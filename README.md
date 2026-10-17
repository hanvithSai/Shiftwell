# Shiftwell: Q4 2026 product recommendation

Response to a product case study for Shiftwell, a fictional shift-scheduling SaaS for multi-location businesses in India (₹4.08 Cr ARR, 8 accounts).

**Live prototype:** https://hanvithsai.github.io/Shiftwell/  
**Submission PDF:** [`report/Shiftwell_Submission.pdf`](report/Shiftwell_Submission.pdf)  
**Repository:** https://github.com/hanvithSai/Shiftwell

## The decision

Build one swap-rules engine instead of three separate features. Every shift assignment is checked for valid credentials, training and weekly hours. Passes are approved instantly, exceptions go to the right person, unsafe assignments are blocked.

| Sprint (two weeks, from 19 Oct 2026) | Ships | Protects |
|---|---|---|
| S1 | Credential gate | CarePoint, renews Dec 2026 |
| S2–3 | Rules engine with auto-approval, FreshBowl pilot | FreshBowl, renews Jan 2027 |
| S4 | Hours-cap rule with approver | UrbanMart, renews Aug 2027 |
| S5–6 | Rollout, then buffer and a WhatsApp decision on pilot data | All |

Not built this quarter: WhatsApp approvals, a custom UrbanMart branch, a full credential suite. The rules-engine estimate (about 2 sprints, range 1.5 to 3) is an assumption pending Engineering.

## What is in this repo

| Path | What it is |
|---|---|
| `report/Shiftwell_Submission.pdf` | The submission: CEO memo, reply to the sales head, assumptions, build note, links, supporting analysis |
| `docs/index.html` | The prototype (served by GitHub Pages from `/docs`) |
| `case/Case_Study.pdf` | The original brief and data pack |
| `report/report.html`, `report/figs/` | Report source and charts |
| `scripts/check_numbers.py` | Recomputes every number quoted in the report from the case tables |
| `scripts/make_charts.py` | Generates the figures |
| `scripts/build_pdf.ps1` | Renders the report to PDF with Edge |

## Prototype

A single HTML file, no backend and no build step. It shows the new swap experience for Staff and Location Manager (mobile), Regional Approver (mobile) and Admin (web), plus a Handoff spec tab for design and engineering: what changes per role, release scope, decision rules, notifications, data model, success metrics and open questions.

- Pick FreshBowl, CarePoint or UrbanMart and follow the guided walkthrough, or send a swap as staff, accept as the colleague and follow it through the other views.
- The **Release** switch shows the product as of Sprint 1, Sprints 2–3 and Sprint 4+.
- All data is synthetic. Nothing connects to customer systems.

To run it locally, open `docs/index.html` in a browser.

## Rebuild the report

```
python scripts/make_charts.py
powershell scripts/build_pdf.ps1
```

Requires Python with matplotlib, and Microsoft Edge.
