"""Builds the report figures from the case-pack numbers. Run: python make_charts.py"""
import datetime as dt
import pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as md
from matplotlib.lines import Line2D

plt.rcParams.update({"font.family": "Segoe UI", "font.size": 9,
                     "axes.spines.top": False, "axes.spines.right": False})
INK, MUT = "#1b2430", "#5f6b7a"
COL = {"Healthy": "#157a55", "Watch": "#c98a0a", "At risk": "#b42318"}
OUT = pathlib.Path(__file__).resolve().parent.parent / "report" / "figs"
OUT.mkdir(parents=True, exist_ok=True)

# name, ARR (lakh), % swaps approved <24h, health
ACC = [("UrbanMart", 110, 64, "Healthy"), ("FreshBowl", 84, 38, "At risk"), ("CarePoint", 60, 71, "At risk"),
       ("QuickKart", 48, 67, "Healthy"), ("Spice Route", 36, 41, "Watch"), ("MedAxis", 30, 80, "Healthy"),
       ("FitZone", 22, 35, "At risk"), ("Brew & Co", 18, 29, "At risk")]
LOST = [("StyleHub", 30, 60), ("TandooriTown", 25, 22), ("GreenLeaf", 16, 31), ("PawsCare", 9, 33)]

# ---- Fig 1: approval speed vs health
fig, ax = plt.subplots(figsize=(6.4, 2.75), dpi=220)
ax.axvspan(18, 45, color="#fdecea", alpha=.55, lw=0)
ax.text(19, 122, "Under 45%: every account here is\nat risk, on watch or already lost", fontsize=8, color="#8d2119", va="top")
for n, a, p, h in ACC:
    ax.scatter(p, a, s=a * 5.5, color=COL[h], alpha=.9, edgecolor="white", lw=.8, zorder=3)
off = {"UrbanMart": (0, 22, "center"), "FreshBowl": (0, 12, "center"), "CarePoint": (0, 15, "center"),
       "QuickKart": (0, -15, "center"), "Spice Route": (0, 13, "center"), "MedAxis": (0, -12, "center"),
       "FitZone": (8, -12, "left"), "Brew & Co": (0, 13, "center")}
for n, a, p, h in ACC:
    dx, dy, ha = off[n]
    ax.annotate(n, (p, a), xytext=(dx, dy), textcoords="offset points", ha=ha, fontsize=8, color=INK)
loff = {"StyleHub": (0, 12, "center"), "TandooriTown": (0, -12, "center"),
        "GreenLeaf": (-4, -26, "center"), "PawsCare": (12, -5, "left")}
for n, a, p in LOST:
    ax.scatter(p, a, s=a * 5.5, facecolor="none", edgecolor=MUT, lw=1.1, ls="--", zorder=2)
    dx, dy, ha = loff[n]
    if n == "StyleHub":
        ax.annotate(n + " 60%", (p, a), xytext=(dx, dy), textcoords="offset points", ha=ha, fontsize=7.5, color=MUT)
ax.text(19, -6, "Dashed = lost: Tandoori 22%, GreenLeaf 31%, PawsCare 33%", fontsize=7, color=MUT, va="center")
ax.set_xlim(18, 86); ax.set_ylim(-12, 130)
ax.set_xlabel("Swaps approved within 24 hours (%)", color=MUT); ax.set_ylabel("ARR (₹ lakh)", color=MUT)
ax.tick_params(colors=MUT)
hnd = [Line2D([], [], marker="o", ls="", color=c, label=k, markersize=6) for k, c in COL.items()]
hnd.append(Line2D([], [], marker="o", ls="", mfc="none", mec=MUT, label="Lost (12 mo)", markersize=6))
ax.legend(handles=hnd, loc="lower left", bbox_to_anchor=(0.5, 0.0), frameon=False, fontsize=8, ncol=2)
fig.tight_layout(); fig.savefig(OUT / "fig1_approval_vs_health.png"); plt.close()

# ---- Fig 2: renewal calendar vs delivery plan
D = dt.date
fig, ax = plt.subplots(figsize=(6.4, 2.45), dpi=220)
sprints = [("S1", D(2026, 10, 19), D(2026, 10, 30), "#1f4fd8"), ("S2-3", D(2026, 11, 2), D(2026, 11, 27), "#1f4fd8"),
           ("S4", D(2026, 11, 30), D(2026, 12, 11), "#1f4fd8"), ("S5", D(2026, 12, 14), D(2026, 12, 25), "#7f98e8"),
           ("S6", D(2026, 12, 28), D(2027, 1, 8), "#c3cff5")]
for i, (lab, s, e, c) in enumerate(sprints):
    ax.barh(2.2, (e - s).days, left=s, height=.45, color=c, edgecolor="white", lw=1.5)
    ax.text(s + (e - s) / 2, 2.2, lab, ha="center", va="center", color="white" if i < 3 else INK,
            fontsize=8, fontweight="bold")
    what = ["Credential\ngate", "Rules engine,\nFreshBowl pilot", "Hours\ncap", "Rollout", "Buffer"][i]
    ax.text(s + (e - s) / 2, 1.93, what, ha="center", va="top", fontsize=7, color=MUT)
ax.text(D(2026, 10, 19), 2.58, "Delivery plan (assumes 2-week sprints from 19 Oct)", fontsize=8, color=MUT)
ax.text(D(2026, 10, 19), 1.32, "Renewals (bubble = ARR; day of month assumed mid-month)", fontsize=8, color=MUT)
ren = [("FitZone", D(2026, 10, 22), 22, "At risk"), ("Brew & Co", D(2026, 11, 18), 18, "At risk"),
       ("CarePoint", D(2026, 12, 15), 60, "At risk"), ("FreshBowl", D(2027, 1, 15), 84, "At risk"),
       ("MedAxis", D(2027, 2, 15), 30, "Healthy"), ("Spice Route", D(2027, 3, 15), 36, "Watch")]
ax.axhline(1.0, color="#dfe4ea", lw=1, zorder=0)
for n, d, a, h in ren:
    ax.scatter(d, 1.0, s=a * 6, color=COL[h], alpha=.9, edgecolor="white", zorder=3)
    ax.annotate(f"{n}\n₹{a}L", (d, 1.0), xytext=(0, -22 if a < 60 else -28), textcoords="offset points",
                ha="center", fontsize=7.5, color=INK)
ax.annotate("UrbanMart (₹110L, healthy) renews Aug 2027  →", (D(2027, 4, 28), 1.0), xytext=(0, 16),
            textcoords="offset points", ha="right", fontsize=7.5, color=MUT)
ax.set_ylim(.15, 2.85); ax.set_xlim(D(2026, 10, 10), D(2027, 4, 30)); ax.set_yticks([])
ax.spines["left"].set_visible(False); ax.tick_params(colors=MUT)
ax.xaxis.set_major_locator(md.MonthLocator()); ax.xaxis.set_major_formatter(md.DateFormatter("%b %y"))
fig.tight_layout(); fig.savefig(OUT / "fig2_renewals_vs_plan.png"); plt.close()

# ---- Fig 3: sprint allocation
fig, ax = plt.subplots(figsize=(6.4, 1.7), dpi=220)
rows = [("Recommended", [("Cert gate", 1, "#1f4fd8"), ("Rules engine", 2, "#4f74e3"), ("Hours cap", 1, "#7f98e8"),
                         ("Rollout", 1, "#a9baf0"), ("Buffer", 1, "#e3e8f6")]),
        ("Sales plan", [("WhatsApp", 3, "#8a94a3"), ("UrbanMart custom", 2, "#b4bcc7"), ("Cert gate", 1, "#1f4fd8")])]
for r, (name, segs) in enumerate(rows):
    x = 0
    for lab, w, c in segs:
        ax.barh(r, w, left=x, height=.6, color=c, edgecolor="white", lw=1.5)
        ax.text(x + w / 2, r, f"{lab}\n{w}", ha="center", va="center", fontsize=7.5,
                color="white" if c in ("#1f4fd8", "#4f74e3", "#8a94a3") else INK)
        x += w
ax.set_yticks([0, 1]); ax.set_yticklabels([r[0] for r in rows], color=INK)
ax.set_xlim(0, 6); ax.set_xlabel("Sprints (6 available)", color=MUT)
ax.spines["left"].set_visible(False); ax.tick_params(colors=MUT, length=0)
fig.tight_layout(); fig.savefig(OUT / "fig3_sprint_allocation.png"); plt.close()
print("figures written to", OUT)
