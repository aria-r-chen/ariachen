# Analysis Folder

This folder contains a lightweight Python reproduction of the portfolio's scoring logic.

## File

`weighted_scoring.py`

The script reproduces:
- the 3.9 / 5 cross-border weighted-selection score
- the 4.3 / 5 U.S. last-mile weighted-selection score
- the 1.90 / 3 overall third-party risk score
- the mapped risk level

## Why standard-library Python?

The goal is transparency and explainability.

The calculations are simple enough that a recruiter or interviewer can audit the logic directly without installing a data-science stack.

## Run

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
