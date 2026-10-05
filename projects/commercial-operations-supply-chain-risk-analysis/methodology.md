# Methodology

## 1. Vendor-Selection Scoring

Each criterion is scored on a 1–5 scale.

**Weighted score**

`Weighted Score = Σ (Criterion Weight × Criterion Score)`

Selection threshold used in the academic case:

- **≥ 3.5 / 5:** passes the selection screen
- **< 3.5 / 5:** does not pass without reconsideration / remediation

The portfolio uses grouped scores for:
- Cross-border: J&T Express / YunExpress
- U.S. last-mile: UPS / USPS

These are the same grouped scores used in the reconstructed academic case.

## 2. Third-Party Risk Rating

The independent dashboard uses a 1–3 risk scale:

- **1 = Low risk / strong evidence and controls**
- **2 = Medium risk / partial evidence or moderate control gaps**
- **3 = High risk / weak evidence, missing controls, or significant concern**

**Overall weighted risk**

`Overall Risk Score = Σ (Category Weight × Category Average Score)`

Management mapping:

| Score | Risk Level | Action |
|---|---|---|
| 1.00–1.50 | Low | Approve / standard monitoring |
| 1.51–2.30 | Medium | Conditional approval + remediation |
| 2.31–3.00 | High | Remediate before onboarding / senior risk acceptance |

The modeled result is **1.90 — Medium**.

## 3. Concentration Constraint

The case uses a management control of:

`Carrier Share ≤ 40%`

Any exception requires senior risk acceptance.

In the synthetic allocation scenario, this becomes an operating constraint rather than only a reporting metric.

## 4. Exception Logic

The portfolio applies the following operating sequence:

`KPI breach → validate → contain exposure → reallocate → escalate → remediate → restore`

This bridges risk governance and supply / commercial operations.

## 5. Why the Model Is Intentionally Simple

This is an early-career analyst portfolio, not a production optimization engine.

The goal is to demonstrate:
- transparent assumptions
- traceable calculations
- business judgment
- management-action linkage
- explainability in an interview

A more advanced future version could add historical carrier data, demand forecasts, cost curves, service-level distributions, and constrained optimization.
