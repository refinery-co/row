# Refinery Row - Formulas and Constants

Every formula below was used on the 2026 vintage. Each carries its source and a worked check against a logged 2026 value. A runnable version with tests is in `refinery_calcs.py` and `test_refinery_calcs.py` in this folder (all checks pass, run with `python3 -m pytest` or `python3 test_refinery_calcs.py`).

Labels used: **[published]** figure from a named source, **[measured]** from James's own batches, **[inference]** derived by Claude and labelled as such.

## Units

| Conversion | Value |
|---|---|
| 1 US gal | 3.78541 L |
| 6.5 gal carboy | 24.61 L (6.51 gal post-MLF = 24.64 L) |
| 1 hL | 100 L |
| ppm in wine | mg/L |

## 1. Alcohol from gravity

`ABV = (OG − FG) × factor`, factor 131.25 (low bound) to 135 (high bound). Both are reported as a range because the factor varies with sugar content.

Check: Sangiovese OG 1.105, FG 1.001 → 13.65 to 14.04%. Cabernet OG 1.100, FG 1.002 → 12.86 to 13.23%. [measured]

## 2. Post-MLF TA (the landing equation)

`post_MLF_TA = TA_start + tartaric_added_gL − 0.56 × malic_gL`

`addition_gL = TA_target − TA_start + 0.56 × malic_gL`

Source: AWRI malolactic fermentation fact sheet: 1 g/L malic contributes 1.12 g/L to TA as tartaric, and complete MLF removes 0.56 g/L TA per 1 g/L malic. [published]

Adding 1 g/L tartaric raises TA by 1 g/L as tartaric (diprotic, MW 150.09, equivalent weight 75.04). [published]

Check: Cabernet 8.36 − 0.56 × 2.96 = 6.70. Sangiovese 9.56 − 0.56 × 3.23 = 7.75. Matches the 09-10 status. [measured inputs]

Caveat: measured post-MLF TA on 09-17 was 6.00 (Cab) and 6.60 (Sangiovese), below both projections. The malic baselines were conservative (in-vial readings above the SC-55 ceiling), so more malic was converted than measured. [inference]

Target band, finished reds: 6.0 to 7.5 g/L (Boulton 1999). WineMaker: 6 to 8. Vinmetrica: 6 to 7. [published]

## 3. Additions by concentration

`grams = g_per_L × litres` and `g_per_L = grams / litres`

`grams = g_per_hL × litres / 100`

Checks: tartaric 83 g / 24.61 L = 3.373 g/L; 58 g / 24.61 L = 2.357 g/L. Opti'Malo Plus 20 g/hL × 24.61 L = 4.92 g. [measured]

## 4. Molecular SO2

`molecular = free / (1 + 10^(pH − pKa))`, pKa 1.81

`free_needed = molecular_target × (1 + 10^(pH − 1.81))`

Targets [published]:

| Context | Molecular target | Source |
|---|---|---|
| Brett prevention | 0.6 mg/L | AWRI |
| Aging, barrel / HDPE / VCT | 0.5 to 0.6 mg/L, check monthly | Pambianchi masterclass slide 9 |
| Aging, glass / stainless | 0.2 to 0.5 mg/L, check every 3 months | Pambianchi masterclass slide 9 |
| Bottling | add 5 to 10 mg/L free | Pambianchi slide 37 |

Checks: pH 3.74 at 0.5 → 43 ppm free. pH 3.96 at 0.6 → 85 ppm free. [arithmetic]

Timing: first SO2 10 to 14 days after MLF completes (Pambianchi slide 9). Dose at 100% on measured pH, re-measure one week later, top up 30 to 50% if short. No SO2 while malic is above 0.05 g/L. [published]

## 5. KMS (potassium metabisulfite) dose

KMS yields about 57.6% SO2 by mass. [published, standard figure]

`ppm_added = grams_KMS × 0.576 × 1000 / litres`

`grams_KMS = ppm_target × litres / (0.576 × 1000)`

Checks: 1.85 g into 24.64 L = 43.2 ppm (Cab, 09-27). 3.0 g into 24.64 L = 70.1 ppm (Sangiovese, 10-11). [measured]

## 6. SO2 bound by acetaldehyde

1 mg acetaldehyde binds 1.45 mg SO2 (mole for mole: 64.07 / 44.05). [published]

`acetaldehyde_mgL = SO2_bound_mgL / 1.45`

Check: 50 to 65 ppm bound → 34 to 45 mg/L acetaldehyde on the Sangiovese (10-12). [inference from a titration with unrecorded sample volume; treat as provisional]

## 7. Dissolved oxygen consumes SO2

1 mg/L DO consumes up to 4 mg/L free SO2. Air-saturated wine (~8 mg/L DO) can consume about 32 ppm. Racking pickup is 0.2 to 2 mg/L O2 without aeration, 3 to 8 with. Source: Pambianchi masterclass slides 32 and 33. [published]

## 8. Free SO2 titration (Vinmetrica SC-300)

`ppm = titrant_mL × multiplier`, multiplier depends on sample volume: 20 at 25 mL, 5 at 100 mL (as recorded in the 10-12 analysis). **The sample volume was never recorded on the 2026 runs, which is why none of them are usable.** Record it every time. Confirm the multiplier against the SC-300 manual before relying on it. [unresolved]

## 9. Malic (Vinmetrica SC-50 / SC-55)

Standard procedure uses a ×2 dilution factor. The vial ceiling is about 1.4 g/L; both 2026 baselines exceeded it in-vial (1.48 and 1.62), so both results are conservative. Next time dilute 1:1 with distilled water before the diluent step and multiply by 4. [published manual + measured]

MLF complete: malic below 0.05 g/L (working threshold). Microbial stability per Pambianchi slide 34: malic below 100 mg/L, RS below 2 g/L. An older note used 0.3 g/L; that is superseded.

## 10. pH response to tartaric

Rule of thumb: about 0.1 pH per 1 g/L, weaker in buffered wine (Vinmetrica). [published]

2026 measured, equilibrated overnight: Sangiovese 0.130 pH per g/L, Cabernet 0.123 pH per g/L. Readings taken 30 minutes after dosing read 0.15 to 0.22 high. [measured]

## 11. Chemistry thresholds

| Threshold | Value | Source |
|---|---|---|
| KHT crossover | pH 3.65. Above, cold stabilization raises pH; below, it lowers pH. | AWRI; Zoecklein and Fugelsang |
| TTB acid cap | 9.0 g/L fixed acid as tartaric in the FINISHED wine | 27 CFR 24.182 |
| OIV acidification limit | 4 g/L | OENO 14/2001 |
| High pH plus high TA | potassium problem, tartaric is the wrong tool | AWRI |

## 12. MLF strain and nutrient

| Item | Value | Source |
|---|---|---|
| Opti'Malo Plus | 20 g/hL; may be added from 48 h before up to the same time as the culture | Lallemand |
| Lalvin VP41 | alcohol to 16%, pH above 3.1, total SO2 to 60 mg/L, min 61F, low diacetyl, 64 to 72F under limiting conditions | Lallemand TDS |
| Viniflora Oenos 2.0 | alcohol 14% (datasheet, Pambianchi) vs up to 15% (Novonesis live page); medium diacetyl | conflict recorded |
| MLF temperature | 68 to 72F (both wines) | VP41 TDS; Pambianchi 64 to 73F |
| Smallest sachets | 66 gal rated (Lallemand 2.5 g, Viniflora 1.5 g), roughly 10x label rate at 6.5 gal | manufacturers |

Pick the strain against projected alcohol before chaptalizing.

## 13. Oak plan (not yet executed)

Reference full dose 91 g (3.70 g/L). Planned French cubes 40 g in the Sangiovese, American 45 g in the Cabernet. Pre-bottling oak chips 2 to 4 g/L (Pambianchi slide 35). Track days on wood, not calendar dates.

## Tools that implement these

- **Pambianchi calculator suite** (© Daniel Pambianchi 2021, `.xlsm`): SO2, YAN, Chaptalization, Amelioration, Blending, Sorbate, Yeast Selection, Conducting TA-pH Trials. Instructions tabs are images inside the workbook (`unzip`, read `xl/media/*.jpg`). These are licensed files; do not publish them.
- **`winecalc.py` / `winemaking-calcs` skill**: deterministic calculator for sugar depletion, chaptalization, tartaric, nutrients, ABV, g/hL and SO2. Source lives on James's Mac, likely under `~/winemaking-calculators/`. Not included in this zip (folder not reachable from this session).
- `refinery_calcs.py` in this folder: a clean reimplementation of the formulas above with tests, written for the handoff as a seed for the GitHub repo.
