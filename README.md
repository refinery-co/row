# Refinery Row

A home winemaker's guide — built from small-batch production in Rodeo, California.

Every section traces back to a source: a lab instrument reading, a published formula, a masterclass reference. Where something is inferred it's labeled as such. Where the science conflicted with what actually happened at the carboy, both are recorded.

**Same streets. New vintages.**

---

## Guide

| Section | What's inside |
|---|---|
| [`guide/grapes/`](guide/grapes/) | Sourcing, lot sheets, Brix/pH/TA at purchase, what to watch for before you buy |
| [`guide/fermentation/`](guide/fermentation/) | Primary fermentation — yeast selection, nutrient timing, chaptalization, gravity tracking |
| [`guide/fermentation/mlf.md`](guide/fermentation/mlf.md) | Malolactic fermentation — strain selection, inoculation, malic monitoring, completion threshold |
| [`guide/corrections/`](guide/corrections/) | Acid additions, deacidification, pH vs TA decisions, bench trial method |
| [`guide/measurements/`](guide/measurements/) | SO2 (free and molecular), TA, malic, pH — instruments, procedures, what the numbers mean |
| [`guide/oak-aging/`](guide/oak-aging/) | Oak format and dose, timing, what to expect by variety |
| [`guide/mead/`](guide/mead/) | Honey selection, nutrient protocol (TOSNA), stabilization, back-sweetening |

---

## Formulas

[`formulas/`](formulas/) — every calculation used in production, with sources and a Python implementation.

```bash
python3 -m pytest formulas/test_refinery_calcs.py -v
```

Every constant carries a source comment. A change that breaks a test must explain why.

---

## Journal

[`journal/`](journal/) — vintage-by-vintage logs. What actually happened at the carboy: lab readings, corrections, bench trial results, tasting notes, lessons. Organized by year.

The guide is built from what the journal teaches.

---

## Refinery Co

Part of the **[Refinery Co](https://github.com/refinery-co)** brand family.

- **[roots](https://github.com/refinery-co/roots)** — plants, growing protocols, collector guide
- **row** — wine and mead (this repo)

Rodeo, CA · 38.0330°N 122.2677°W
