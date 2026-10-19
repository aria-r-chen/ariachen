# Digital Growth & Content Operations: Bosch Heating Retail (DRAFT)

> **Portfolio reconstruction in progress.** The work supported a family-owned heating-product retail/service business. This repository is not an official Bosch project, headquarters dataset, or brand endorsement. No private customer records or confidential financials are included.

## Core business problem
How can a regional heating-products seller convert short-form-video reach into **qualified inquiries**, usable sales handoffs, and an efficient repeatable content workflow?

## Three connected modules
1. **Commercial funnel / KPI analysis:** compare views → inquiries → qualified leads → completed purchases. Demo in \`analytics/kpi_summary.py\` uses synthetic data only, with no attribution/profit claims.
2. **Creative brief → editor-ready packet:** structured scene durations, voiceover, overlay text, footage keys and quality checks. \`automation/build_editor_pack.py\` produces \`shotlist.csv\` and \`editor_prompt.md\`. This does not generate a video or synchronize actual footage.
3. **Operating controls / evidence:** verify product specifications, sales promises, data definitions, contribution boundaries, consumer privacy and footage licenses before publication.

## Workflow
\`\`\`bash
python analytics/kpi_summary.py analytics/example_campaigns_SYNTHETIC.csv
python automation/build_editor_pack.py content/example_video_brief.json --outdir output/demo
\`\`\`

**Editor integration limitation:** A portable prompt is not universal automation. To remove manual editing, first standardize assets/timecodes, then implement and validate an editor-specific import/API adapter (e.g., for a specific CapCut/Jianying or other tool where supported), followed by final human commercial/claims QA.

## Project status
- Framework, demo data, portable video-brief prototype: created; usable for *testing*.
- Actual company data, the user's Muse analysis, market segmentation, business outcome evidence: **awaiting review**.
- Automated assembly in an external editor and automated publishing: **not implemented**.
- Original resume fact bank includes several growth metrics; they are intentionally not claimed here until sources and individual contributions are reconciled. See [evidence register](docs/evidence_register.md).

## Portfolio standard
Separate **my own role**, **team/company outcome**, **demonstration assumptions** and **verified customer impact**. Never treat synthetic demo outputs as actual performance or state causal impact without supporting evidence.