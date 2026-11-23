# Refinery Row

> *Same streets. New vintages.*

A home winemaker's guide built from real production in Rodeo, California. Every number has a source. Every inference is labeled. Where the science conflicted with what actually happened at the carboy, both are recorded.

---

## Guide

| | |
|---|---|
| [🍇 Grapes](guide/grapes/) | Reading the lot sheet, high-pH fruit, ABV planning, 100 lb checklist |
| [🧪 Primary Fermentation](guide/fermentation/) | Yeast selection, chaptalization, nutrients, temperature |
| [🦠 MLF](guide/fermentation/mlf.md) | Strain selection, inoculation timing, malic monitoring, SO2 after completion |
| [⚗️ Corrections](guide/corrections/) | Landing equation, bench trials, when tartaric is the wrong tool |
| [📊 Measurements](guide/measurements/) | SO2 (free and molecular), TA, malic, pH — instruments, procedures, what the numbers mean |
| [🪵 Oak & Aging](guide/oak-aging/) | Format, dose, American vs French, timing, prerequisites |
| [🍯 Mead](guide/mead/) | Coming soon |

---

## Formulas

[`formulas/`](formulas/) — every calculation in production, with sources and a Python implementation. All tests reproduce logged 2026 values.

```bash
python3 -m pytest formulas/test_refinery_calcs.py -v
```

> Every constant carries a source comment. A change that breaks a test must explain why.

---

## Journal

[`journal/`](journal/) — vintage by vintage. Lab readings, corrections, bench trial results, tasting notes, lessons learned.

The guide is built from what the journal teaches.

---

Part of [Refinery Co](https://github.com/refinery-co) · Rodeo, CA · 38.0330°N 122.2677°W
