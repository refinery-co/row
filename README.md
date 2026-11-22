# Refinery Row

Small-batch wine and mead made in Rodeo, California, under the name Refinery Row Wines.

The same waterfront strip of Contra Costa County that defined Rodeo for over a century — crude in, product out — is now a renewable energy plant. The wine is made in the town that grew up around it. Same streets. New vintages.

---

## 2026 Vintage

| Carboy | Varietal | Source | Status |
|---|---|---|---|
| RR-2026-CAB-01 | Cabernet Sauvignon | Suisun Valley | MLF complete — not yet racked or oaked |
| RR-2026-SAN-01 | Sangiovese | Tehama County | MLF complete — SO2 and acetaldehyde work pending |

Both wines finished MLF by October 2026. See [`OPEN-ITEMS.md`](OPEN-ITEMS.md) for current state and next steps.

---

## What's Here

| Folder | Contents |
|---|---|
| [`formulas/`](formulas/) | Every calculation used on the 2026 vintage — acid, SO2, ABV, chaptalization — with sources and a Python implementation |
| [`history/`](history/) | Vintage notebooks, MLF outcome, acid and correction notes, masterclass reference figures |
| [`OPEN-ITEMS.md`](OPEN-ITEMS.md) | Current wine state, overdue work, next steps in order |

---

## The Calculation Library

`formulas/refinery_calcs.py` is a clean Python implementation of every formula with tests that reproduce logged 2026 values. Run the tests:

```bash
python3 -m pytest formulas/test_refinery_calcs.py -v
```

Every constant carries a source comment. A change that breaks a test must explain why.

---

## Refinery Co

Part of the **[Refinery Co](https://github.com/refinery-co)** brand family.

- **[roots](https://github.com/refinery-co/roots)** — plants, growing protocols, collector guide
- **row** — wine, mead (this repo)

Both grounded in Rodeo, California.
