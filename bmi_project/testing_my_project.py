import pytest
import bmi
import kalorie


def test_oblicz_bmi():
    assert bmi.oblicz_bmi(52,150) == int(52 / (150/100) ** 2)

def test_zapotrzebowanie_kaloryczne_kobiet():
    result = kalorie.zapotrzebowanie_kaloryczne_kobiet(52, 150, 15, 2)
    assert int(result) == int((10 * 52 + 6.25 * 150 - 5 * 15 - 161) * 1.4)

def test_zapotrzebowanie_kaloryczne_mężczyzn():
    result = kalorie.zapotrzebowanie_kaloryczne_mężczyzn(62, 180, 17, 4)
    assert int(result) == int((10 * 62 + 6.25 * 180 - 5 * 17 + 5) * 1.8)

