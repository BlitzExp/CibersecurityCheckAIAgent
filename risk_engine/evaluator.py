from typing import Dict, List

from risk_engine.rules import RiskLevel
from sources.cve_nvd import fetch_cves_for_library


def evaluate_library(library: Dict) -> Dict:
    """
    Evaluates the security risk of a single library using CVE data.
    """
    name = library.get("name")
    version = library.get("version")

    cves = fetch_cves_for_library(name)

    if not cves:
        risk = RiskLevel.SAFE
        reason = "No known CVEs found in public databases"
        recommendation = "Keep dependency updated"
    else:
        high_severity = any(
            cve.get("cvss_score") is not None and cve["cvss_score"] >= 7.0
            for cve in cves
        )

        if high_severity:
            risk = RiskLevel.INSECURE
            reason = "High severity vulnerabilities detected in public CVE database"
            recommendation = (
                "Upgrade to a patched version or apply mitigations immediately"
            )
        else:
            risk = RiskLevel.DOUBTFUL
            reason = (
                "Known vulnerabilities exist, but none rated as high severity"
            )
            recommendation = "Review CVEs and monitor for updates"

    return {
        "library": name,
        "version": version,
        "risk": risk.value,
        "reason": reason,
        "recommendation": recommendation,
        "cves": cves
    }


def evaluate_stack(libraries: List[Dict]) -> List[Dict]:
    """
    Evaluates the entire stack of libraries.
    """
    results = []

    for lib in libraries:
        assessment = evaluate_library(lib)
        results.append(assessment)

    return results