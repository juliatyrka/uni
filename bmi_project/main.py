import sys
from bmi import oblicz_bmi
from kalorie import zapotrzebowanie_kaloryczne_kobiet
from kalorie import zapotrzebowanie_kaloryczne_mężczyzn
from osoby import Osoba

def main():
    waga = float(input("Podaj swoją wagę (kg): "))
    wzrost = int(input("Podaj swój wzrost (cm): "))
    wiek = int(input("Podaj swój wiek: "))
    plec = input("Podaj swoją płeć (m/k): ").lower()
    aktywnosc = input("Podaj poziom aktywności z zakresu 1-6, gdzie 1 to najniższa: ")

    if plec == 'k':
       wynik = zapotrzebowanie_kaloryczne_kobiet(waga, wzrost, wiek, aktywnosc)
       bmi = oblicz_bmi(waga,wzrost)
       print(f"Twoje zapotrzebowanie kaloryczne: {wynik}")
       print(f"Twoje BMI: {bmi}")
    elif plec == 'm':
       wynik = zapotrzebowanie_kaloryczne_mężczyzn(waga, wzrost, wiek, aktywnosc)
       bmi = oblicz_bmi(waga,wzrost)
       print(f"Twoje zapotrzebowanie kaloryczne: {wynik}")
       print(f"Twoje BMI: {bmi}")
    else:
       raise ValueError('Podano niewłaściwą płeć')

    osoby = []
    Ania = Osoba('Anna','Nowak',62,172,32,'k',2)
    osoby.append(Ania)
    print(osoby)

if __name__ == "__main__":
    main()
