# Shiftwell: Q4 2026 product recommendation

Case study response for Shiftwell, a fictional shift-scheduling SaaS for multi-location businesses in India.

**Recommendation:** build one swap-rules engine instead of three separate features. It checks credentials, training and weekly hours when someone is assigned a shift, auto-approves what passes, escalates exceptions and blocks unsafe assignments. Sequence: credential gate (1 sprint), rules engine (about 2), hours-cap rule (about 1), rollout, buffer. No WhatsApp approvals or custom UrbanMart build this quarter.

## Contents

| Path | What it is |
|---|---|
| `report/Shiftwell_Submission.pdf` | Submission: CEO memo, sales reply, assumptions, build note, links |
| `docs/index.html` | Working prototype: clickable multi-role demo and handoff spec (GitHub Pages serves `/docs`) |
| `case/Case_Study.pdf` | Original brief and data pack |
| `report/report.html`, `report/figs/` | Report source and charts |
| `scripts/` | `make_charts.py` (figures), `build_pdf.ps1` (HTML to PDF with Edge) |

## Prototype

Open `docs/index.html` in a browser, no build step. A clickable demo of the new swap experience for Staff and Location Manager (mobile), Regional Approver (mobile) and Admin (web), plus a **Handoff spec** tab for design and engineering: decision table, screen inventory by sprint, notifications, data model, edge cases. Pick FreshBowl, CarePoint or UrbanMart, send a swap as staff, accept as the colleague, and follow it through the manager, approver and admin views. All data is synthetic.
