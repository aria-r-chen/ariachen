"""Simple weighted-scoring demonstration for the Temu portfolio case.

This script intentionally uses only Python's standard library so the logic
remains easy to audit and explain in an interview.
"""

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
    return sum(scores[key] * weights[key] for key in weights)


def risk_level(score):
    if score <= 1.50:
        return "Low"
    if score <= 2.30:
        return "Medium"
    return "High"


if __name__ == "__main__":
    print("Vendor selection weighted scores")
    for name, scores in selection_scores.items():
        score = weighted_score(scores, selection_weights)
        print(f"- {name}: {score:.2f} / 5.00")

    overall_risk = sum(weight * score for weight, score in risk_categories.values())
    print("\nThird-party risk rating")
    print(f"- Overall weighted risk score: {overall_risk:.2f} / 3.00")
    print(f"- Risk level: {risk_level(overall_risk)}")
