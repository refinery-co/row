# Malolactic Fermentation (MLF)

MLF converts sharp malic acid to softer lactic acid. It softens the wine, adds complexity, and — critically — provides microbial stability. For red wines in glass aging, it is not optional.

---

## When to Inoculate

Inoculate MLF at the end of primary fermentation or at press — not before. Inoculating too early wastes the culture and can create off-flavors if alcohol rises too fast for the bacteria.

Minimum conditions before inoculating:
- SG below 1.010 (preferably near dry)
- Free SO2 below 20 ppm (bacteria are SO2-sensitive)
- Temperature above 61°F (VP41) / 59°F (Oenos 2.0)
- pH above 3.1

---

## Strain Selection

| Strain | Alcohol ceiling | pH floor | Diacetyl | Notes |
|---|---|---|---|---|
| Lalvin VP41 | 16% | 3.1 | Low | Cold-tolerant (61°F min). Best under limiting conditions. |
| Viniflora Oenos 2.0 | 14–15% | 3.1 | Medium | Conflict: 14% (Pambianchi/datasheet) vs 15% (Novonesis live page) — use 14% as the ceiling. |

**Pick the strain against projected alcohol before chaptalizing.** If chaptalization pushes ABV above 14%, Oenos 2.0 may not complete MLF.

---

## Nutrients

Opti'Malo Plus: **20 g/hL** (not 1 g/gal — that older figure is superseded). May be added from 48 hours before up to the same time as the culture.

---

## Monitoring

Monitor malic acid with the Vinmetrica SC-55.

- **In-vial ceiling:** approximately 1.4 g/L. If the starting malic reads at the ceiling (1.4+ g/L), dilute 1:1 with distilled water before the diluent step and multiply result by 4.
- **Complete:** malic below **0.05 g/L** (working threshold). Pambianchi slide 34: below 100 mg/L (0.1 g/L) for microbial stability — use 0.05 g/L as the conservative threshold.
- Do not add SO2 while malic is above 0.05 g/L.

---

## The TA Math

MLF removes acid — plan for it.

`TA drop = 0.56 × malic acid (g/L)`

A wine starting at 2 g/L malic loses 1.12 g/L TA through MLF. If the target finished TA is 6.5 g/L and MLF will drop TA by 1.12, the pre-MLF TA target is 7.62 g/L.

Use the landing equation to plan acid additions:

`post-MLF TA = starting TA + tartaric added − (0.56 × malic)`

This is why malic measurement before acid additions matters. The 2026 Cabernet and Sangiovese malic readings both hit the SC-55 ceiling, so the baseline was conservative and more malic was converted than modeled.

---

## Temperature

68–72°F for both VP41 and Oenos 2.0. The 72–77°F target used in early 2026 planning was revised to 68–72°F — the lower end prevents VA production.

---

## SO2 After MLF

Dose SO2 within 10–14 days of MLF completion (Pambianchi slide 9).

- Do not wait. Every day after MLF without SO2 is exposure at high pH.
- Dose at 100% of target, then re-measure one week later and top up 30–50% if short.
- For glass: target **0.2–0.5 mg/L molecular** SO2 (not the barrel number of 0.5–0.6).

See [`../measurements/so2.md`](../measurements/so2.md) for the full SO2 calculation.

---

## Sources

- Lallemand VP41 technical data sheet
- Viniflora Oenos 2.0 / Novonesis product page
- AWRI, Malolactic fermentation fact sheet
- Pambianchi masterclass slides 9, 34
