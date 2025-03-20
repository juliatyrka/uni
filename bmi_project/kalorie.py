def zapotrzebowanie_kaloryczne_kobiet(waga, wzrost, wiek, aktywnosc):
    '''Oblicza zapotrzebowanie kaloryczne dla kobiet'''
    zap = 10 * waga + 6.25 * wzrost - 5 * wiek - 161
    if aktywnosc == 1:
        zap *= 1.2
    elif aktywnosc == 2:
        zap *= 1.4
    elif aktywnosc == 3:
        zap *= 1.6
    elif aktywnosc == 4:
        zap = zap * 1.8
    elif aktywnosc == 5:
        zap = zap * 2.0
    elif aktywnosc == 6:
        zap = zap * 2.4
    return int(zap)


def zapotrzebowanie_kaloryczne_mężczyzn(waga, wzrost, wiek, aktywnosc):
    '''Oblicza zapotrzebowanie kaloryczne dla mężczyzn'''
    zap = 10 * waga + 6.25 * wzrost - 5 * wiek + 5
    if aktywnosc == 1:
        zap *= 1.2
    elif aktywnosc == 2:
        zap *= 1.4
    elif aktywnosc == 3:
        zap *= 1.6
    elif aktywnosc == 4:
        zap = zap * 1.8
    elif aktywnosc == 5:
        zap = zap * 2.0
    elif aktywnosc == 6:
        zap = zap * 2.4
    return int(zap)