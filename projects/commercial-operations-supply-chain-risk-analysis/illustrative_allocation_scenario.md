# Illustrative Allocation & Exception-Handling Scenario

> **Portfolio extension — synthetic scenario.**  
> This operating scenario was created to demonstrate how the original concentration-risk and KPI/KRI framework can translate into day-to-day allocation decisions. It is not presented as Temu's actual carrier allocation or internal operating data.

## Objective

Allocate U.S. last-mile volume across a diversified carrier pool while balancing:
- service reliability
- concentration risk
- backup capacity
- operational continuity
- escalation discipline

The original academic case proposed a **40% concentration threshold**: no single carrier should exceed 40% of parcel volume without senior risk acceptance.

## Baseline Allocation

Assume a planning batch of **1,000 U.S. last-mile shipments**.

| Carrier | Role | Baseline Allocation | Share | Status |
|---|---|---:|---:|---|
| UPS | Primary commercial / urban carrier | 400 | 40% | At concentration limit |
| USPS | Primary universal-access carrier | 400 | 40% | At concentration limit |
| Backup Carrier X | Pre-qualified contingency capacity | 200 | 20% | Available reserve |
| **Total** |  | **1,000** | **100%** |  |

This mix respects the 40% threshold and keeps pre-qualified backup capacity active rather than purely theoretical.

## Trigger Event

During the monitoring cycle, assume UPS falls below the required service threshold because of a material delivery-delay issue.

Illustrative exception:
- on-time delivery falls below target
- SLA breach trend worsens
- expected delay persists into the next planning cycle

## Reallocation Decision

Temporarily reduce UPS exposure and reallocate volume without allowing any carrier to exceed the 40% concentration threshold.

| Carrier | Before | After Exception | Change |
|---|---:|---:|---:|
| UPS | 400 / 40% | 200 / 20% | -200 |
| USPS | 400 / 40% | 400 / 40% | 0 |
| Backup Carrier X | 200 / 20% | 400 / 40% | +200 |
| **Total** | **1,000 / 100%** | **1,000 / 100%** |  |

## Exception-Handling Logic

1. **Detect** — KPI/KRI monitoring identifies a sustained service issue.
2. **Validate** — confirm that the signal is not a one-off data-quality problem.
3. **Contain** — stop increasing volume to the affected carrier.
4. **Reallocate** — shift volume to pre-qualified capacity while respecting concentration limits.
5. **Escalate** — open an issue with an owner, due date, and remediation requirement.
6. **Review** — restore volume only after service performance recovers and remediation evidence is accepted.

## Why This Matters

The purpose of a concentration threshold is not just reporting. It should influence real operating decisions.

This scenario converts a risk-control statement into an execution rule:

**KPI deterioration → allocation change → issue escalation → remediation → controlled restoration of volume.**

That is the link between third-party risk governance and commercial / supply-chain operations.
