# Refinery Row: Index

What is in this project, what is on James's machine, and which one is authoritative. Last updated 2026-09-10.

---

## Read this first

**The cellar log is the source of truth, and it is not in this project.** It lives at `~/Documents/Refinery Row/Vintage 2026/Refinery Row 2026 - Cellar Log.xlsx`. Nothing here supersedes it. If a number in this project disagrees with the log, the log is right.

These project docs are the shareable layer: state, journal, and reference. They are mirrors, kept current by hand.

## What is in this project

| Doc | What it is | Update when |
|---|---|---|
| `00-index.md` | This file | The structure changes |
| `refinery-row-2026-status.md` | **Live vintage status.** Batch summary, per-batch chronology, remaining sequence, open items. | Any decision or measurement changes the plan |
| `vintage-notebook-carry-forward.md` | **The journal.** What happened, what it cost, what to do differently. One document across all vintages, a section per year. | End of a working session, or when a lesson lands |
| `acid-addition-and-mlf-notes.md` | Sourced chemistry reference | A figure is added, corrected, or retracted |

## Naming convention

Kebab-case, no year in the filename except where the doc is genuinely vintage-specific. `refinery-row-2026-status.md` carries the year because next vintage gets its own status doc; `vintage-notebook-carry-forward.md` does not, because it is one running document forever.

An index sorts first because of the `00-` prefix. Nothing else gets a number prefix.

## What is on the machine and not here

The local folder holds the working files and the reference library. Its own map is `~/Documents/Refinery Row/INDEX.pdf`.

```
Refinery Row/
├── INDEX.pdf / .md            <- the local map
├── Vintage 2026/              <- cellar log, bench trials, SOP, README, journal
├── Tools/                     <- Pambianchi calculator suite, pristine
│   └── 2026 Working Copies/   <- calculators with 2026 numbers typed in
└── Wine Knowledge Base/       <- reference library plus sourced notes
```

**Sourced notes in `Wine Knowledge Base/`**, every figure cited. Check these before searching the web.

- Acid Management and MLF
- TA Measurement, Vinmetrica SC-300
- Malic Measurement, Vinmetrica SC-50 kit
- MLF Bacteria Strain Selection, all five suppliers' tables transcribed
- Competition Targets, acid and pH for award wines
- Grape Sourcing, Oak Barrel lot data and site notes
- Redox and Reduction Risk, post-fermentation handling
- Pambianchi Masterclass and Redox Control, operative numbers

Each exists as **both `.md` and `.pdf`**. The PDF is for reading, the Markdown is the source, and the PDF is regenerated from it rather than edited. If the two disagree, the Markdown is right.

## Conventions that apply to every doc here

**Every figure carries a source.** No invented thresholds, no rule of thumb presented as guidance. Distinguish published figures, locally measured data, and inference, and label inference as inference.

**Cross-check anything load-bearing against a second source.** Manufacturer pages, technical datasheets and Pambianchi's book tables regularly disagree. When they do, record the conflict and say which reading is being used and why.

**Corrections are written down, not quietly fixed.** A retraction with its reason is more useful than a clean document that hides a wrong turn. Several entries in the journal are walk-backs and they are the most valuable part of it.
