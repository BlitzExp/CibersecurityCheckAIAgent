import requests

NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def fetch_cves_for_library(library_name: str, max_results: int = 5) -> list:
    """
    Fetches recent CVEs related to a library name from NVD.
    Returns a list of simplified CVE entries.
    """
    params = {
        "keywordSearch": library_name,
        "resultsPerPage": max_results
    }

    try:
        response = requests.get(NVD_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"⚠️ Error fetching CVEs for {library_name}: {e}")
        return []

    vulnerabilities = []

    for item in data.get("vulnerabilities", []):
        cve = item.get("cve", {})
        cve_id = cve.get("id")
        description_data = cve.get("descriptions", [])
        description = description_data[0]["value"] if description_data else ""

        metrics = cve.get("metrics", {})
        cvss_score = None

        if "cvssMetricV31" in metrics:
            cvss_score = metrics["cvssMetricV31"][0]["cvssData"]["baseScore"]
        elif "cvssMetricV30" in metrics:
            cvss_score = metrics["cvssMetricV30"][0]["cvssData"]["baseScore"]

        vulnerabilities.append({
            "cve_id": cve_id,
            "description": description,
            "cvss_score": cvss_score
        })

    return vulnerabilities
