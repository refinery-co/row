# Refinery Row 2026 - carboy label check log

> Handoff note: run log of the daily scheduled label refresh. The 11-22 and 11-05 entries are verbatim. The 11-15 to 11-21 entries were all no-change runs on identical inputs and are condensed here; the full text is in the Claude project doc `label-check-log.md`.

Label source: `~/Documents/Refinery Row/Labels/Carboy Labels 2026 - source.html`
Log: `~/Documents/Refinery Row/Refinery_Row_2026_Log.xlsx`

## 2026-11-22 - no change, no reprint, no notification sent

**Label state: correct and current. Not reprinted.**

Seventh consecutive run on identical inputs. Log mtime 2026-10-12 00:54 UTC, 119,279 bytes, md5 df40a47602dad0d305d93524465f2e76. Label source 2026-10-12 15:08 UTC, 8,364 bytes, md5 bdc817a533604dcf34abdbdfa7e43d32; PRINT pdf 261,656 bytes. The label is still newer than the log. PLANNED NEXT STEPS still starts at Cabernet row 62 and Sangiovese row 75, and the last populated row above it is still Cabernet 61 and Sangiovese 74, both dated 2026-10-12, so no label field moved.

Both files re-staged and all sixteen fields re-derived from the most recent non-empty cell per column, nothing carried forward: TA pre-MLF 9.56 / 8.36 (col J rows 43 and 34), pH 3.96 / 3.74 (col K rows 73 and 60), malic baseline 3.23 / 2.96 (col Q rows 39 and 36), ABV 13.65-14.04% / 12.86-13.23%, tartaric 83 g / 3.37 g/L and 58 g / 2.36 g/L, free SO2 ruled blank on both (col L holds only the 08-27 zero at rows 13 and 12, col M entirely empty), yeast BM 4X4 / BDX, ML strain VP41 / Oenos 2.0, nutrient Opti'Malo Plus 4.9 g (col C rows 53 and 44, logged as 4.92 g), oak French / American cubes (rows 52 and 43, both still marked PLANNED), racked 09-08 / 09-07, MLF start 09-10 both (col Q Started, rows 55 and 46), MLF done 10-11 / 09-27 (col Q rows 68 and 55), volume 6.51 gal both (col E), TA footer 6.60 / 6.00 g/L from 09-17 (col J rows 63 and 53), first free SO2 target 71 ppm at pH 3.96 and 43 ppm at pH 3.74. Header note already reads 2026-10-12. MLF hold temperature and malic check cadence correctly absent, retired by the 10-12 travel row.

No threshold crossed. Cabernet post-MLF pH is 3.74, above the 3.65 crossover, so the held-open acid decision stays held. Malic cleared on both wines (Cabernet none detectable 09-27, Sangiovese 0.10 g/L on 09-27 then below 0.05 g/L on 10-11) and both are sulfited, so neither the stalling-MLF case nor the 10 to 14 day SO2 wait is live.

**No entry in the log for 41 days**, and 30 days back from travel with nothing recorded. The silence has now passed the 40-day mark the 11-21 run flagged, but the rule that run set is explicit: raise the silence itself at the next run in December, not before. Held, so this run sent nothing.

**The overdue free SO2 re-measure was again not notified.** Seventh consecutive run on the same unchanged item, now 35 days past the 10-18 or 10-19 one-week confirmation. Neither wine has a verified free SO2 figure, neither has been racked post-MLF, oak is out of both. Unchanged, so not re-raised.

**Lock files.** Still no ~$ lock on the log workbook, so what is on disk is complete and nothing was guessed. The two orphaned 2026-09-08 locks are unchanged and neither feeds a label. No action.

**Still unlogged outside its own column.** Unchanged. All three titration volumes (Cab 6.3 mL and 4.49 mL, Sangiovese 1.0 mL) and every estimated ppm figure exist only in column R prose, so none can go on a label.

**Still pending for the next real reprint.** The Cabernet label prints Racked 2026-09-07, the press into bucket and jug; the rack into the carboy is the 09-08 row. Change it whenever the sheet is next reprinted for a reason of its own. Not worth a sheet of film by itself.

## 2026-11-15 through 2026-11-21 - five no-change runs, condensed

All ran on byte-identical inputs (log 2026-10-12 00:54 UTC, 119,279 bytes; label source md5 bdc817a533604dcf34abdbdfa7e43d32). No reprint, no notification. Rules set during these runs that still stand:

- A repeat push on an unchanged item is noise; the overdue SO2 re-measure is not re-notified.
- If the log is still untouched at the first December run, raise the 40-plus day silence itself as the new point.
- **Correction 11-17:** the `YEAST SELECTION PLANNER v1.0.xlsm` lock file is 3.5 hours newer than its last save (19:53 vs 16:22 UTC on 09-08), so anything typed after 16:22 UTC that day was never saved. The planner's output (BM 4X4 Sangiovese, BDX Cabernet) is already executed and logged. The `Bench_Trials_2026.xlsm` lock (21:04 UTC) is older than its save (22:29 UTC). Both locks can be deleted.

## 2026-11-05 - no change, no reprint. Notified about the overdue SO2 re-measure.

**Label state: correct and current. Not reprinted.**

The label source was rendered 2026-10-12 15:08 UTC. The log was last saved 2026-10-12 00:54 UTC. The label is newer than the log, and the last populated row on both sheets is still 2026-10-12, so nothing has been logged since the labels were made.

| Field | RR-2026-SAN-01 | RR-2026-CAB-01 | Matches log |
|---|---|---|---|
| pH | 3.96 (10-11) | 3.74 (09-27) | yes, col K |
| Volume | 6.51 gal | 6.51 gal | yes, col E |
| TA in footer | 6.60 g/L (09-17) | 6.00 g/L (09-17) | yes, col J |
| MLF done | 2026-10-11 | 2026-09-27 | yes, col Q |
| Free SO2 | ruled blank | ruled blank | yes, col L holds only the 08-27 zero |

**What is overdue, and why it was worth a notification.** The 10-11 and 10-12 SO2 protocol calls for a free SO2 re-measure one week after the addition, which fell on 10-18 or 10-19. On the Sangiovese that measurement is not routine monitoring: roughly 50 to 65 ppm of the 10-11 dose bound inside 24 hours, implying 35 to 45 mg/L acetaldehyde, and free SO2 on that wine has never been measured successfully. Free and total together give the bound fraction, which is the only direct read on that load.

Note that the Pambianchi glass-and-stainless cadence of every 3 months is not what is overdue here. The one-week confirmation after a dose is.
