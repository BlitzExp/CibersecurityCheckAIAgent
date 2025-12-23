from datetime import datetime


def generate_markdown_report(
    stack: dict,
    results: list,
    output_path: str = "security_report.md"
):
    project = stack.get("project", "Unknown")
    environment = stack.get("environment", "Unknown")

    total = len(results)
    insecure = sum(1 for r in results if r["risk"] == "INSECURE")
    doubtful = sum(1 for r in results if r["risk"] == "DOUBTFUL")
    safe = sum(1 for r in results if r["risk"] == "SAFE")

    lines = []

    lines.append("# Stack Security Report\n")
    lines.append(f"_Generated on {datetime.utcnow().isoformat()} UTC_\n")

    lines.append("## Project Information\n")
    lines.append(f"- **Project:** {project}")
    lines.append(f"- **Environment:** {environment}\n")

    lines.append("## Summary\n")
    lines.append(f"- Total libraries analyzed: {total}")
    lines.append(f"- 🔴 Insecure: {insecure}")
    lines.append(f"- 🟡 Doubtful: {doubtful}")
    lines.append(f"- 🟢 Safe: {safe}\n")

    lines.append("---\n")
    lines.append("## Dependency Analysis\n")

    for r in results:
        risk_icon = {
            "INSECURE": "🔴",
            "DOUBTFUL": "🟡",
            "SAFE": "🟢"
        }.get(r["risk"], "⚪")

        lines.append(f"### {risk_icon} {r['library']} ({r['version']})\n")
        lines.append(f"**Risk Level:** `{r['risk']}`  ")
        lines.append(f"**Reason:** {r['reason']}  ")
        lines.append(f"**CVEs Found:** {len(r.get('cves', []))}\n")

        if r.get("ai_explanation"):
            lines.append("#### AI Risk Explanation\n")
            lines.append(r["ai_explanation"].strip() + "\n")

        lines.append("#### Recommended Action\n")
        lines.append(f"- {r['recommendation']}\n")
        lines.append("---\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))