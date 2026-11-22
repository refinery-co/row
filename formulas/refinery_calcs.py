"""Refinery Row winemaking calculations.

Seed module for the refinery-row-calcs repo. Every function cites its source
in FORMULAS.md. Pure functions, no I/O, standard library only.
"""
from __future__ import annotations

L_PER_GAL = 3.78541
SO2_PKA = 1.81
KMS_SO2_FRACTION = 0.576        # potassium metabisulfite yields ~57.6% SO2 by mass
MALIC_TA_DROP = 0.56            # AWRI: g/L TA lost per g/L malic after complete MLF
SO2_PER_ACETALDEHYDE = 1.45     # mg SO2 bound per mg acetaldehyde (64.07 / 44.05)
SO2_PER_DO = 4.0                # Pambianchi slide 33: up to 4 mg/L SO2 per mg/L DO
KHT_CROSSOVER_PH = 3.65         # AWRI
TTB_FINISHED_TA_CAP = 9.0       # 27 CFR 24.182, finished wine


def gal_to_l(gal: float) -> float:
    return gal * L_PER_GAL


def abv_range(og: float, fg: float) -> tuple[float, float]:
    """ABV low/high using the 131.25 and 135 factors."""
    d = og - fg
    return round(d * 131.25, 2), round(d * 135, 2)


def post_mlf_ta(ta_start: float, tartaric_gl: float, malic_gl: float) -> float:
    """Landing equation (AWRI): TA after complete MLF."""
    return round(ta_start + tartaric_gl - MALIC_TA_DROP * malic_gl, 2)


def tartaric_for_target(ta_target: float, ta_start: float, malic_gl: float) -> float:
    """g/L tartaric needed so post-MLF TA lands on target. Negative means none."""
    return round(ta_target - ta_start + MALIC_TA_DROP * malic_gl, 3)


def grams_from_gl(g_per_l: float, litres: float) -> float:
    return g_per_l * litres


def gl_from_grams(grams: float, litres: float) -> float:
    return grams / litres


def grams_from_ghl(g_per_hl: float, litres: float) -> float:
    return g_per_hl * litres / 100


def molecular_so2(free_ppm: float, ph: float) -> float:
    return free_ppm / (1 + 10 ** (ph - SO2_PKA))


def free_so2_needed(molecular_target: float, ph: float) -> float:
    return molecular_target * (1 + 10 ** (ph - SO2_PKA))


def kms_ppm_added(grams_kms: float, litres: float) -> float:
    return grams_kms * KMS_SO2_FRACTION * 1000 / litres


def kms_grams_for_ppm(ppm: float, litres: float) -> float:
    return ppm * litres / (KMS_SO2_FRACTION * 1000)


def acetaldehyde_from_bound_so2(bound_so2_mgl: float) -> float:
    return bound_so2_mgl / SO2_PER_ACETALDEHYDE


def so2_consumed_by_do(do_mgl: float) -> float:
    """Upper bound on free SO2 consumed by dissolved oxygen."""
    return do_mgl * SO2_PER_DO


def cold_stab_ph_direction(ph: float) -> str:
    """Direction KHT precipitation moves pH (AWRI crossover)."""
    if ph > KHT_CROSSOVER_PH:
        return "raises"
    if ph < KHT_CROSSOVER_PH:
        return "lowers"
    return "neutral"


def ttb_compliant(finished_ta: float) -> bool:
    """Applies to FINISHED wine only, never a pre-MLF value."""
    return finished_ta <= TTB_FINISHED_TA_CAP
