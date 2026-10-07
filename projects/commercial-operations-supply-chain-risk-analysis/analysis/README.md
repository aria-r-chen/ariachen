# Analysis Folder

This folder contains a lightweight, auditable Python reproduction of the portfolio's scoring logic.

## Files

- `weighted_scoring.py` — reproduces the weighted vendor-selection and third-party risk calculations.
- `test_weighted_scoring.py` — regression tests for weights, scores, risk bands, and management-action mapping.

## What the model reproduces

- **3.90 / 5** cross-border weighted-selection score
- **4.30 / 5** U.S. last-mile weighted-selection score
- **1.895 / 3** raw third-party risk score, displayed as **1.90 / 3**
- **Medium** risk classification
- **Conditional approval + remediation plan** management action

## Why standard-library Python?

The goal is transparency and interview explainability rather than software-engineering complexity. A reviewer can audit the formulas directly without installing a data-science stack.

## Run the model

```bash
python weighted_scoring.py
```

Expected output:

```text
Vendor selection weighted scores
- cross_border_group: 3.90 / 5.00 — PASS
- us_last_mile_group: 4.30 / 5.00 — PASS

Third-party risk rating
- Overall weighted risk score: 1.90 / 3.00
- Risk level: Medium
- Management action: Conditional approval + remediation plan
```

## Run the tests

From this `analysis/` folder:

```bash
python -m unittest -v
```

The current suite contains **5 regression checks** covering:

1. vendor-selection weights sum to 100%;
2. both published selection scores are reproducible;
3. third-party risk weights sum to 100%;
4. the raw 1.895 score and displayed 1.90 score are both validated;
5. Low / Medium / High risk-band boundaries map correctly.

GitHub Actions also runs these tests automatically when the analysis files change.

> These tests validate arithmetic and mapping logic only. They do not validate real-world carrier performance or imply access to non-public Temu data.
