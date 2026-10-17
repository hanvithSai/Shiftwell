"""Recomputes every derived number quoted in the report from the case-pack tables."""
# name, segment, locations, ARR lakh, renewal (yyyy-mm), staff, swaps/mo, % <24h, LM hrs/wk, health
A = [("UrbanMart", "Retail", 200, 110, "2027-08", 5200, 3100, 64, 3.5, "Healthy"),
     ("FreshBowl", "Restaurants", 120, 84, "2027-01", 3600, 2900, 38, 6.5, "At risk"),
     ("CarePoint", "Clinics", 40, 60, "2026-12", 900, 310, 71, 4.0, "At risk"),
     ("QuickKart", "Retail", 90, 48, "2027-06", 2100, 1000, 67, 3.0, "Healthy"),
     ("Spice Route", "Restaurants", 60, 36, "2027-03", 1500, 1400, 41, 6.0, "Watch"),
     ("MedAxis", "Diagnostics", 25, 30, "2027-02", 450, 90, 80, 2.5, "Healthy"),
     ("FitZone", "Gyms", 50, 22, "2026-10", 600, 540, 35, 5.5, "At risk"),
     ("Brew & Co", "Cafes", 35, 18, "2026-11", 700, 820, 29, 7.0, "At risk")]
LOST = [("StyleHub", "Retail", 70, 30, 60, "Budget cuts"), ("TandooriTown", "Restaurants", 45, 25, 22, "Price"),
        ("GreenLeaf", "Restaurants", 30, 16, 31, "RotaPro (WhatsApp)"), ("PawsCare", "Clinics", 15, 9, 33, "Spreadsheets")]

tot = sum(a[3] for a in A)
print(f"Total ARR {tot} lakh (case: 408)  | locations {sum(a[2] for a in A)} | staff {sum(a[5] for a in A)} | swaps/mo {sum(a[6] for a in A)}")
ar = [a for a in A if a[9] == "At risk"]; wt = [a for a in A if a[9] == "Watch"]
print(f"At risk {sum(a[3] for a in ar)}L ({sum(a[3] for a in ar)/tot:.0%}); + watch {sum(a[3] for a in ar+wt)}L ({sum(a[3] for a in ar+wt)/tot:.0%})")
by_mar = [a for a in A if a[4] <= "2027-03"]
print(f"Renewing by Mar 2027: {sum(a[3] for a in by_mar)}L ({sum(a[3] for a in by_mar)/tot:.0%}); of which at risk/watch {sum(a[3] for a in by_mar if a[9]!='Healthy')}L")
print(f"Renewing by Jan 2027 (before/at FreshBowl): {sum(a[3] for a in A if a[4] <= '2027-01')}L")
low = [a for a in A if a[7] < 45]
print(f"Accounts <45% on 24h approvals: {[a[0] for a in low]} -> health {set(a[9] for a in low)}; ARR {sum(a[3] for a in low)}L ({sum(a[3] for a in low)/tot:.0%}); swaps {sum(a[6] for a in low)} of {sum(a[6] for a in A)} ({sum(a[6] for a in low)/sum(a[6] for a in A):.0%})")
print("Lost: total", sum(l[3] for l in LOST), "L; opening base", tot + sum(l[3] for l in LOST), f"; gross churn {sum(l[3] for l in LOST)/(tot+sum(l[3] for l in LOST)):.1%}")
print("Lost restaurants:", sum(l[3] for l in LOST if l[1] == 'Restaurants'), "L; lost <=33% approval:", [l[0] for l in LOST if l[4] <= 33])
print("Shift-heavy segment (restaurants, cafes, gyms) now:", sum(a[3] for a in A if a[1] in ('Restaurants', 'Cafes', 'Gyms')), "L, health:", {a[0]: a[9] for a in A if a[1] in ('Restaurants', 'Cafes', 'Gyms')})
print("LM hrs/wk, shift-heavy:", [a[8] for a in A if a[1] in ('Restaurants', 'Cafes', 'Gyms')], "others:", [a[8] for a in A if a[1] not in ('Restaurants', 'Cafes', 'Gyms')])
print("\nPer account: ARR/location (L) | swaps/location/mo | swaps/staff/mo | 24h-misses/mo")
for a in A:
    print(f"  {a[0]:12s} {a[3]/a[2]:.2f} | {a[6]/a[2]:5.1f} | {a[6]/a[5]:.2f} | {round(a[6]*(100-a[7])/100)}")
fb = A[1]
print(f"\nFreshBowl: {fb[6]/fb[2]:.1f} swaps/location/mo; manager claim 25-30/night = {27.5*30:.0f}/mo = {27.5*30/(fb[6]/fb[2]):.0f}x average")
print(f"Approval effort at avg volume, 5-10 min each: {fb[6]/fb[2]*5/60:.1f}-{fb[6]/fb[2]*10/60:.1f} h/month vs {fb[8]*52/12:.0f} h/month scheduling")
print(f"UrbanMart share of ARR {110/tot:.0%}; months to renewal from Oct 2026: 10; clinics+diagnostics {90}L = {90/tot:.0%} on {65/sum(a[2] for a in A):.0%} of locations")
print(f"WhatsApp: 4 msgs x Rs0.35 x {fb[6]} = Rs{4*0.35*fb[6]:,.0f}/mo = Rs{4*0.35*fb[6]*12/1e5:.2f}L/yr (all accounts: Rs{4*0.35*sum(a[6] for a in A)*12/1e5:.2f}L/yr)")
print("Sprints: sales plan 3+2+1 =", 3+2+1, "| recommended 1+2+1+1+1 =", 1+2+1+1+1, "| 2-wk sprints from 19 Oct -> S5 ends 25 Dec, S6 ends 8 Jan")
