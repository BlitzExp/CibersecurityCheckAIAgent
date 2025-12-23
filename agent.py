import json
from pathlib import Path

from llm.explainer import generate_explanation
from risk_engine.evaluator import evaluate_stack
from reporting.markdown import generate_markdown_report


def load_stack(path: str):
    with open(path, "r") as f:
        return json.load(f)

def main():
    stack_path = Path("stack.json")

    if not stack_path.exists():
        print("❌ stack.json not found")
        return

    stack = load_stack(stack_path)

    print("Security Check Agent")
    print(f"Project: {stack.get('project')}")
    print(f"Environment: {stack.get('environment')}\n")

    libraries = stack.get("libraries", [])
    results = evaluate_stack(libraries)

    print("Risk Assessment:\n")

    for r in results:
        print(f"🔹 {r['library']} ({r['version']})")
        print(f"   Risk: {r['risk']}")
        print(f"   Reason: {r['reason']}")
        print(f"   Recommendation: {r['recommendation']}")
        print(f"   CVEs found: {len(r.get('cves', []))}")

        explanation = generate_explanation(r)
        print("\n AI Explanation:")
        print(explanation)
        print("\n" + "-" * 50 + "\n")
    
    generate_markdown_report(stack, results)
    print("📄 Markdown report generated: security_report.md")

if __name__ == "__main__":
    main()
