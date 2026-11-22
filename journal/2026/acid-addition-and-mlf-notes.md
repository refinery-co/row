# Acid Additions and MLF - Reference Notes

> Handoff note: written 2026-09-08, before TA and malic were measured. The sourced ranges, the AWRI MLF math and the regulatory table remain valid. The "Current state" table at the bottom and the 4.00 g/L / 2.50 g/L decisions were superseded the same day once TA was measured (final: Sangiovese 83 g, Cabernet 58 g post-press). The "US TTB" row is also superseded: 27 CFR 24.182 caps acid additions at 9.0 g/L fixed acid in the finished wine.

For the RR-2026 tartaric decisions. Every number below is sourced; sources listed at the end.

## Published target ranges

**TA in finished red wine**

| Source | Range for reds |
|---|---|
| Boulton (1999), via Winemakers Research Exchange | 6.0 to 7.5 g/L |
| Jackson (2014), via WRE | 5.5 to 8.5 g/L overall, reds at the lower end |
| Zoecklein, via WRE | 5.0 to 16 g/L (broad) |
| Vinmetrica (maker of the SC-300) | 6 to 7 g/L target; below 5 or above 10 is a candidate for adjustment |
| WRE field data, Virginia reds 2014-2020 | Cab Franc and Merlot averaged 4.2 to 4.5; Petit Verdot 7.2 |

Working band: **6.0 to 7.5 g/L**, with a high-acid variety like Sangiovese comfortable in the upper half and a Cabernet better in the lower half.

**pH in red wine**

- Vinmetrica: target 3.2 to 3.5 at fermentation start; "anything above pH 4.0 is likely to need adjustment."
- AWRI: adjust red musts to pH 3.4 or lower, "regardless of the amount of tartaric acid required to do so."

Note both are stricter than the RR-2026 decisions (Cab 3.55, Sangiovese 3.62). On pH grounds alone the references argue for going further, not less.

## The MLF math, quantified

AWRI's malolactic fermentation fact sheet gives the exact relationship:

- Each 1 g/L of malic acid contributes **1.12 g/L** to TA expressed as tartaric.
- After complete MLF, TA drops by **0.56 g/L for every 1 g/L of malic acid originally present**.
- Worked example from AWRI: a wine with 2 g/L malic loses 1.12 g/L of TA.

Vinmetrica adds the pH side: expect **+0.1 to +0.2 pH** on completion of MLF.

So the TA drop is not a fixed "1 to 2 g/L." It depends entirely on the malic concentration, which is measurable on the SC-55.

## The landing equation

**Post-MLF TA = starting TA + tartaric added − (0.56 × malic acid)**

Rearranged to size the addition against a target:

**Addition = target TA − starting TA + (0.56 × malic)**

At a typical red malic of 2.0 g/L, aiming for a post-MLF TA of 7.0:

| Starting TA | Addition to land at 7.0 | Resulting pH (Sangiovese curve) |
|---|---|---|
| 4.0 | 4.1 g/L | ~3.62 |
| 4.5 | 3.6 g/L | ~3.65 |
| 5.0 | 3.1 g/L | ~3.68 |
| 5.5 | 2.6 g/L | ~3.74 |
| 6.0 | 2.1 g/L | ~3.78 |

The current Sangiovese decision of 4.00 g/L is correct only if starting TA is roughly 4.0 to 4.5. Above that it overshoots the Boulton band.

## Tartaric response

Vinmetrica's rule: pH drops about 0.1 per 1 g/L of tartaric, but "this relationship weakens in high-TA wines due to buffering effects."

Measured on RR-2026:

- **Cabernet:** 0.14 pH per g/L. Linear across all five steps. Responds better than the rule.
- **Sangiovese:** 0.106 pH per g/L average, with a flat shoulder of 0.03 to 0.04 through the 2.0 to 3.0 g/L stretch.

That shoulder is the buffering Vinmetrica describes, and it is indirect evidence the Sangiovese carries more TA than the Cabernet.

## When tartaric is the wrong tool

High pH together with high TA is the signature of high potassium, not of acid deficiency. In that state, added tartaric raises TA without moving pH much, which is the worst of both outcomes. The remedy is potassium removal through KHT precipitation, not more acid.

The KHT crossover is about **pH 3.65** (AWRI): above it, precipitation raises pH while TA falls; below it, precipitation lowers pH while TA falls. Both wines sit above the crossover now and will sit at or below it after correction, so winter cold stabilization will nudge pH down rather than up once they are adjusted.

## Staged addition: three independent sources agree

- **Pambianchi** (CONDUCTING TA-PH TRIALS v1.0, STEP 6): "add half the calculated amount of acid to your juice/must, measure TA and pH, and add/adjust the second half."
- **Pambianchi** again (Amelioration Calculator v1.0): splits water additions in two for the same reason, because red must volume is an estimate.
- **Vinmetrica:** "add half the amount of adjustment chemicals that you think you need, then re-check pH and TA to see where you are."

## Regulatory benchmarks

| Benchmark | Limit |
|---|---|
| OIV (Resolution OENO 14/2001) | 4 g/L as tartaric, must and wine combined |
| EU, wine | 2.5 g/L |
| EU, must | 1.5 g/L |
| US TTB | No g/L cap; commercial wine capped at 9.0 g/L total fixed acidity |

These bind commercial producers, not a home cellar. They are useful as sanity markers only. RR-2026 Sangiovese at 4.00 g/L sits exactly at the OIV ceiling; the Cabernet at 2.50 g/L sits exactly at the EU wine limit.

## Tasting check

Pambianchi (CONDUCTING TA-PH TRIALS v1.0, STEP 5): "Do NOT taste samples as that would change the sample size and acid additions. You can however taste the Decision sample at the conclusion of the trials to make sure you are not acidifying excessively."

Both Decision samples were tasted. Cabernet at 3.55 tasted good. Sangiovese at 3.66 was tart but smoothed, not shrill.

## SO2 and pH

Molecular SO2 = free SO2 / (1 + 10^(pH − 1.81)).

| pH | Free SO2 for 0.6 molecular | What 30 ppm free delivers |
|---|---|---|
| 3.50 | 30 ppm | 0.60 |
| 3.62 | 40 ppm | 0.45 |
| 3.75 | 54 ppm | 0.33 |
| 4.03 | 100 ppm | 0.18 |

The plan's 25 to 35 ppm free SO2 target only functions near pH 3.5, which is another argument for the fuller corrections.

## Current state (superseded, see handoff note)

| | Volume | pH now | Decision | Dose | TA | Malic |
|---|---|---|---|---|---|---|
| Cabernet | 6.5 gal | 3.90 | 2.50 g/L to 3.55 | 61.5 g | not measured | not measured |
| Sangiovese | 6.5 gal | 4.03 | 4.00 g/L to 3.62 | 98.4 g | not measured | not measured |

## Sources

- [Vinmetrica, Managing pH and TA in wine](https://vinmetrica.com/managing-ph-and-ta-in-wine/)
- [AWRI, Malolactic fermentation fact sheet (PDF)](https://www.awri.com.au/wp-content/uploads/2011/06/Malolactic-fermentation.pdf)
- [AWRI, Acidity and pH FAQ](https://www.awri.com.au/industry_support/winemaking_resources/frequently_asked_questions/acidity_and_ph/)
- [Winemakers Research Exchange, How to Interpret Titratable Acidity Results](https://winemakersresearchexchange.com/library/fermentation/how-to-interpret-titratable-acidity-results/)
- [OIV, Maximum limits for acidification](https://www.oiv.int/node/3744)
- [WineWiki, Tartaric Acid Addition](https://www.winewithseth.com/winewiki/tartaric-acid-addition-acidification/)
- Daniel Pambianchi, CONDUCTING TA-PH TRIALS v1.0 and Amelioration Calculator v1.0, INSTRUCTIONS tabs (local files)
