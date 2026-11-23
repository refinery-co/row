# Measurements

Every number needs a source, a timestamp, and a sample volume. Numbers without these cannot be acted on safely.

---

## SO2 — Free and Molecular

### Why It Matters

Free SO2 is what protects the wine. Molecular SO2 (the active fraction) is what matters for microbial stability. The same 30 ppm free SO2 delivers very different molecular SO2 at different pH levels.

### The Formula

`molecular SO2 = free SO2 / (1 + 10^(pH − 1.81))`

`free SO2 needed = target molecular × (1 + 10^(pH − 1.81))`

### Targets by Vessel

| Vessel | Molecular SO2 target | Check frequency |
|---|---|---|
| Barrel, HDPE, VCT | 0.5–0.6 mg/L | Monthly |
| Glass, stainless | 0.2–0.5 mg/L | Every 3 months |
| Brett prevention | 0.6 mg/L | — |

Source: Pambianchi masterclass slide 9. **Glass needs less than barrel** — common mistake is using the barrel number for glass.

### Free SO2 at Common pH Levels

| pH | Free needed for 0.5 molecular | Free needed for 0.6 molecular |
|---|---|---|
| 3.50 | 25 ppm | 30 ppm |
| 3.65 | 36 ppm | 44 ppm |
| 3.75 | 43 ppm | 52 ppm |
| 3.96 | 71 ppm | 85 ppm |
| 4.00 | 79 ppm | 95 ppm |

Formula uses pKa 1.81 (Pambianchi / standard winemaking reference).

### KMS Dose

`grams KMS = target ppm × litres / (0.576 × 1000)`

KMS yields 57.6% SO2 by mass.

`ppm added = grams KMS × 0.576 × 1000 / litres`

### Procedure (Vinmetrica SC-300)

1. Record: sample volume, date, titrant volume (mL)
2. Record the multiplier used (20 at 25 mL sample, 5 at 100 mL sample) — verify against SC-300 manual
3. The sulfite electrode and pH electrode are separate sensors — calibrate each independently
4. Dose at 100% of calculated target
5. Re-measure one week later; top up 30–50% if short
6. Total SO2 minus free = bound. High bound fraction relative to what was added indicates acetaldehyde binding.

### Acetaldehyde Binding

`acetaldehyde (mg/L) = SO2 bound (mg/L) / 1.45`

1 mg acetaldehyde binds 1.45 mg SO2 (mole-for-mole: 64.07 / 44.05).

If a large SO2 addition vanishes within 24 hours, binding — not loss — is the likely cause. The implied acetaldehyde load can be estimated from the difference between expected and measured free SO2.

---

## TA — Titratable Acidity

TA measures total acid load as tartaric equivalents. Use the Vinmetrica SC-300 or standard NaOH titration.

- Target for reds: **6.0–7.5 g/L** (Boulton 1999)
- Below 5 g/L: flat, lacks freshness
- Above 8 g/L: aggressive tartness, candidate for deacidification
- Measure before any acid additions, after MLF completion, and after cold stabilization

---

## Malic Acid

Use Vinmetrica SC-55.

- **In-vial ceiling:** approximately 1.4 g/L. Starting malic in high-acid musts often exceeds this. Dilute 1:1 with distilled water before the diluent step and multiply by 4.
- **MLF complete threshold:** below 0.05 g/L. Do not add SO2 until malic is confirmed below this.
- Measure before acid additions (baseline for landing equation) and to confirm MLF completion.

---

## pH

- Calibrate the pH electrode before each use — a cream of tartar check validates the electrode.
- The pH electrode and sulfite electrode (SC-300) are separate: validating one does not validate the other.
- Readings taken 30 minutes after a tartaric addition will read 0.15–0.22 higher than overnight equilibrated values. Wait overnight before deciding to add more.

---

## Dissolved CO2

If a wine tastes tart despite TA and pH being in range, dissolved CO2 is the most likely cause. Run the shake-and-compare test:
1. Pour two samples
2. Shake one vigorously for 30 seconds to degas
3. Taste both
4. If the shaken sample tastes significantly less tart, CO2 is the culprit — not acid excess

Do not deacidify on tartness alone without ruling out CO2.

---

## Sources

- Pambianchi masterclass slides 9, 32, 33, 34, 37
- Vinmetrica SC-300 and SC-55 manuals
- AWRI, Malolactic fermentation fact sheet
- Standard winemaking reference: KMS 57.6% SO2 by mass
