"""Transparent weighted-scoring demonstration for the Temu portfolio case.

The script intentionally uses only Python's standard library so the logic
remains easy to audit and explain in an interview.
"""

SELECTION_THRESHOLD = 3.5

selection_weights = {
    "cross_border_capability": 0.15,
    "us_last_mile_coverage": 0.15,
    "cost_efficiency": 0.15,
    "delivery_reliability": 0.15,
    "data_security": 0.10,
    "compliance_capability": 0.10,
    "subcontractor_oversight": 0.10,
    "resilience": 0.10,
}

selection_scores = {
    "cross_border_group": {
        "cross_border_capability": 5,
        "us_last_mile_coverage": 2,
        "cost_efficiency": 5,
        "delivery_reliability": 4,
        "data_security": 4,
        "compliance_capability": 4,
        "subcontractor_oversight": 3,
        "resilience": 4,
    },
    "us_last_mile_group": {
        "cross_border_capability": 2,
        "us_last_mile_coverage": 5,
        "cost_efficiency": 4,
        "delivery_reliability": 5,
        "data_security": 5,
        "compliance_capability": 5,
        "subcontractor_oversight": 4,
        "resilience": 5,
    },
}

risk_categories = {
    "Strategies and Goals": (0.05, 1.50),
    "Legal and Regulatory Compliance": (0.08, 1.50),
    "Financial Condition": (0.06, 2.00),
    "Business Experience": (0.05, 1.00),
    "Key Personnel and Human Resources": (0.04, 2.00),
    "Risk Management": (0.08, 2.00),
    "Information Security": (0.15, 2.00),
    "Management of Information Systems": (0.07, 2.00),
    "Operational Resilience": (0.12, 2.00),
    "Incident Reporting and Management": (0.08, 2.00),
    "Physical Security": (0.04, 1.00),
    "Reliance on Subcontractors": (0.10, 2.50),
    "Insurance Coverage": (0.06, 2.00),
    "External Contractual Commitments": (0.02, 2.00),
}


def weighted_score(scores, weights):
    """Return the weighted average for a score dictionary."""
    return sum(scores[key] * weights[key] for key in weights)


def risk_level(score):
    """Map the 1–3 weighted score to the portfolio risk bands."""
    if score <= 1.50:
        return "Low"
    if score <= 2.30:
        return "Medium"
    return "High"


def management_action(score):
    """Map the risk score to a management response."""
    level = risk_level(score)
    if level == "Low":
        return "Approve / standard monitoring"
    if level == "Medium":
        return "Conditional approval + remediation plan"
    return "Remediate before onboarding / senior risk acceptance"


if __name__ == "__main__":
    print("Vendor selection weighted scores")
    for name, scores in selection_scores.items():
        score = weighted_score(scores, selection_weights)
        result = "PASS" if score >= SELECTION_THRESHOLD else "REVIEW"
        print(f"- {name}: {score:.2f} / 5.00 — {result}")

    overall_risk = sum(weight * score for weight, score in risk_categories.values())

    print("\nThird-party risk rating")
    print(f"- Overall weighted risk score: {overall_risk:.2f} / 3.00")
    print(f"- Risk level: {risk_level(overall_risk)}")
    print(f"- Management action: {management_action(overall_risk)}")
