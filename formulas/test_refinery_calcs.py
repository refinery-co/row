"""Each test reproduces a value logged on the 2026 vintage."""
import math

import refinery_calcs as rc

CARBOY_L = 24.61
POST_MLF_L = 24.64


def close(a, b, tol=0.06):
    return math.isclose(a, b, abs_tol=tol)


def test_abv():
    assert rc.abv_range(1.105, 1.001) == (13.65, 14.04)
    assert rc.abv_range(1.100, 1.002) == (12.86, 13.23)


def test_post_mlf_ta():
    assert rc.post_mlf_ta(8.36, 0, 2.96) == 6.70
    assert rc.post_mlf_ta(9.56, 0, 3.23) == 7.75


def test_tartaric_gl():
    assert close(rc.gl_from_grams(83, CARBOY_L), 3.373, 0.001)
    assert close(rc.gl_from_grams(58, CARBOY_L), 2.36, 0.005)


def test_opti_malo():
    assert close(rc.grams_from_ghl(20, CARBOY_L), 4.92, 0.005)


def test_free_so2_targets():
    assert close(rc.free_so2_needed(0.5, 3.74), 43, 0.5)
    assert close(rc.free_so2_needed(0.6, 3.96), 85, 0.5)
    assert close(rc.free_so2_needed(0.6, 3.90), 74, 0.5)


def test_kms():
    assert close(rc.kms_ppm_added(1.85, POST_MLF_L), 43.2, 0.1)
    assert close(rc.kms_ppm_added(3.0, POST_MLF_L), 70.1, 0.1)


def test_acetaldehyde():
    assert close(rc.acetaldehyde_from_bound_so2(50), 34.5, 0.1)
    assert close(rc.acetaldehyde_from_bound_so2(65), 44.8, 0.1)


def test_do():
    assert rc.so2_consumed_by_do(8) == 32


def test_thresholds():
    assert rc.cold_stab_ph_direction(3.74) == "raises"
    assert rc.cold_stab_ph_direction(3.60) == "lowers"
    assert rc.ttb_compliant(7.75)
    assert not rc.ttb_compliant(9.56)  # only meaningful on finished wine


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
