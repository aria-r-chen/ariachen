# Temu Logistics: Buy vs. Build, Vendor Selection & Third-Party Risk Controls

## Executive Summary

This portfolio case evaluates whether Temu should **build an in-house U.S. logistics network** or **buy logistics capability through third-party providers**.

The recommendation is a **conditional BUY**: use a diversified two-layer carrier model — **J&T Express / YunExpress** for cross-border line-haul and **UPS / USPS** for U.S. last-mile delivery — subject to explicit service, concentration, data-protection, and fourth-party controls.

The analysis combines:
- business-model and operating-model assessment
- buy-vs.-build decision analysis
- weighted vendor-selection scoring
- KPI / KRI design
- third-party due diligence and risk rating
- confidential-data controls
- implementation and monitoring governance

## Business Problem

Temu's asset-light model creates a strategic trade-off:

**Build:** own logistics infrastructure, fleets, facilities, systems, staffing, and operating complexity.

**Buy:** leverage existing logistics providers for faster market access, variable-cost capacity, and specialist expertise — while accepting third-party execution, concentration, data, compliance, and subcontractor risk.

The objective is not to eliminate risk. It is to choose the operating model with the best strategic fit and then make the residual risk governable.

## Decision Framework

### 1. Buy vs. Build

The BUY case is stronger on:
- capital discipline
- speed to market
- flexibility during promotions and peak demand
- access to logistics and customs expertise
- management focus on Temu's core marketplace capabilities

The BUILD case offers more direct control, but requires significant fixed investment and exposes Temu to asset-utilization, labor, safety, insurance, technology, and transportation complexity.

### 2. Vendor Selection

The academic case used eight weighted criteria and a 3.5 / 5 selection threshold.

| Criterion | Weight | Cross-Border Group | U.S. Last-Mile Group |
|---|---:|---:|---:|
| Cross-border capability | 15% | 5 | 2 |
| U.S. last-mile coverage | 15% | 2 | 5 |
| Cost efficiency | 15% | 5 | 4 |
| Delivery reliability | 15% | 4 | 5 |
| Data security | 10% | 4 | 5 |
| Compliance capability | 10% | 4 | 5 |
| Subcontractor oversight | 10% | 3 | 4 |
| Resilience | 10% | 4 | 5 |
| **Weighted total** | **100%** | **3.9** | **4.3** |

The two-layer structure assigns providers to the lane where they are strongest rather than relying on one carrier for the full chain.

See: [vendor_selection_scorecard.csv](vendor_selection_scorecard.csv)

## Independent Third-Party Risk Rating Model

As a separate individual assignment, I built a structured third-party risk rating dashboard using a 1–3 risk scale, category weights, due-diligence questions, evidence notes, weighted scoring, and management actions.

**Overall weighted score: 1.90 / 3.00 — Medium Risk**

**Management action: Conditional approval + remediation plan**

The highest-risk area in the model was **Reliance on Subcontractors**, reinforcing the importance of fourth-party visibility, approval rights, contractual flow-down, and auditability.

See: [risk_rating_dashboard.csv](risk_rating_dashboard.csv)

## Key Controls & Monitoring

The control framework focuses on risks that can directly affect customer experience, business continuity, data protection, and regulatory exposure.

- **Operational / service risk:** SLA commitments, on-time delivery, loss/damage rate, peak-capacity requirements, route contingency, backup-carrier readiness.
- **Data privacy & confidentiality:** data minimization, DPA, encryption, role-based access, logging, no secondary use, deletion / return at offboarding, 24-hour incident notification.
- **Regulatory / customs risk:** compliance attestations, documentation standards, audit rights, regulatory-change notification.
- **Concentration risk:** no single carrier above 40% of parcel volume without senior risk acceptance.
- **Fourth-party risk:** subcontractor inventory, approval rights, contractual flow-down, audit rights, incident reporting.
- **Ongoing monitoring:** monthly KPI / KRI review, issue escalation, annual reassessment, renew / remediate / replace decisions.

See: [controls_monitoring_framework.md](controls_monitoring_framework.md)

## Implementation Roadmap

**Phase 1 — Validate & Pilot**
- complete due diligence
- negotiate SLAs, data and audit controls
- pilot selected logistics lanes
- validate delivery performance and customer experience

**Phase 2 — Scale & Diversify**
- increase volume gradually
- maintain multi-carrier routing
- enforce concentration thresholds
- validate peak-season capacity

**Phase 3 — Optimize & Govern**
- continuous KPI / KRI monitoring
- periodic vendor reviews
- annual risk reassessment
- remediation, renewal, or replacement decisions

## My Contribution

The original Temu case was developed as a six-person Columbia University team project.

My primary ownership was:
- TPRM risk and control assessment
- confidential-data handling and governance analysis
- public-source research supporting those sections
- integration and coordination across team workstreams
- design and construction of most of the final presentation
- synthesis of the final management recommendation

I also completed the companion third-party risk rating dashboard as an **independent individual assignment**.

The course permitted and expected AI-assisted work. AI was used as a support tool during the academic project; final source selection, risk judgment, framework integration, presentation design, and management conclusions were reviewed and owned by me.

## Portfolio Reconstruction

This repository is an **independent portfolio reconstruction** of academic work. It does not reproduce teammates' personal information or present team contributions as solely mine.

Some business-value figures from the classroom deck are intentionally omitted here because they require source-level validation before being presented as decision-grade facts.

## Skills Demonstrated

**Operations & Analytics**
- structured decision analysis
- weighted scoring
- KPI / KRI design
- vendor performance monitoring
- operating-model evaluation
- implementation planning

**Risk & Controls**
- third-party risk management
- due diligence
- control design
- concentration risk
- fourth-party risk
- confidential-data governance
- issue escalation and residual-risk acceptance

**Tools**
- Excel / spreadsheet modeling
- Power Query, PivotTables, XLOOKUP / VLOOKUP, IF / SUMIFS
- PowerPoint
- Python (coursework)
- Java (coursework)
- R (coursework)

## Sources & Scope

The academic case used course materials and public sources including PDD Holdings filings, UPS and USPS public materials, the 2023 Interagency Guidance on Third-Party Relationships, and other public references.

This is a portfolio case study for analytical demonstration, not investment advice, legal advice, or an assertion of Temu's actual internal vendor contracts, allocation percentages, or control environment.
