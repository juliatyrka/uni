import sys
from bmi import oblicz_bmi
from kalorie import zapotrzebowanie_kaloryczne_kobiet
from kalorie import zapotrzebowanie_kaloryczne_mężczyzn

class Osoba:
    def __init__(self, imie, nazwisko, waga, wzrost, wiek, plec, aktywnosc):
        self.imie = imie
        self.nazwisko = nazwisko
        self.waga = waga
        self.wzrost = wzrost
        self.wiek = wiek
        self.plec = plec
        self.aktywnosc = aktywnosc

    def __str__(self):
        return f"Imię: {self.imie}, Nazwisko: {self.nazwisko}, Wiek: {self.wiek}, Płeć: {self.plec}, Waga: {self.waga}kg, Wzrost: {self.wzrost}cm"

    def bmi(self):
        return oblicz_bmi(self.waga, self.wzrost)
