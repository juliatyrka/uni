import math as math
from random import randint
from abc import ABC, abstractmethod
import random

#lista 1,2,3
#1
x=5
print(x)
#2
user = (input("Podaj swoje imię:")).capitalize()
print('Twoje imię:',user)
#3

def wiek_emerytalny(w,p):
    '''Wiek - w,
     płeć - p, może być wyrażone jako m lub k'''
    if p == 'k':
      if w >= 60:
          print('Kwalifikuje się do emerytury')
      elif w < 60:
          print("Nie kwalifikuje się")
      elif w <= 0:
          raise ValueError('Wiek nie może być ujemny')
    elif p=='m':
       if w >= 65:
           print('Kwalifikuje się do emerytury')
       elif w<65:
           print("Nie kwalifikuje się")
       elif w<=0:
           raise ValueError('Wiek nie może być ujemny')


wiek_emerytalny(60,'k')

#4
class is_it_triangle():
    def __init__(self,a,b,c):
       '''Funkcja, która sprawdza, czy podane boki a,b,c mogą utworzyć trojkąt'''
       self.a,self.b,self.c=a,b,c

       if a+b>c and a+c>b and b+c>a:
           print('To jest trojkąt')
       else:
           print('To nie jest trójkąt')


#ćw 4, ćw 5

#1
students={'imię':['Kasia',"Ania",'Basia'],'nazwisko':['Nowak','Kowalska','Kloc'],'wiek':[19,21,22]}
print(f"Imię: {students['imię'][0]}, Nazwisko: {students['nazwisko'][0]}, Wiek: {students['wiek'][0]}")

#2
krotka = ("Anna", "Jan","Maria") #Nie można dodać nowej osoby, krotki są immutable

#3
list_of_num = [5,2,8,1,3]
list_of_num.sort(reverse=False)
list_of_num.pop(1)
print(list_of_num)

#4
workers = [['Adam','Nowak','dyrektor',7800],['Filip','Kowalski','praktykant',2870],['Barbara','Kloc','kierownik',5200]]
for worker in workers:
    imie, nazwisko, stanowisko, pensja = worker
    if pensja > 5000:
        print(f"Imię: {imie}, Nazwisko: {nazwisko}, Stanowisko: {stanowisko}, Pensja: {pensja}")

#5
z_dict = {1: {'imię': 'Agnieszka', 'nazwisko':'Gogołowska','wiek':15}, 2:{'imię':'Jakub', 'nazwisko':"Student",'wiek':21}}
print(z_dict[1]['imię'])

#6
z_tuple = ((1,2,3),(4,5,6))
print(z_tuple[0][2])

#ćw 6
#1
names = ['Anna', 'Jan', 'Maria']
surnames = ['Kowalska', 'Nowak', 'Wiśniewska']
def full_name(names, surnames):
    return [f"{name} {surname}" for name, surname in zip(names, surnames)]
print(full_name(names, surnames))

#2
grades = [2,3,4,5]
for index, grade in enumerate(grades):
    print(f'Ocena: {grade}, Indeks: {index}')

#3
items = {'matematyka', 'historia', 'informatyka'}
print(len(items))

#4
from collections import deque

q = deque()

def add_to_queue(element):
    q.append(element)
    print(f"Dodano {element} do kolejki.")

def del_queue():
    if q:
        element = q.popleft()
        print(f"Usunięto {element} z kolejki.")
    else:
        print("Kolejka jest pusta.")

def show_queue():
    if q:
        print("Zawartość kolejki:", list(q))
    else:
        print("Kolejka jest pusta.")

add_to_queue('test')
show_queue()
del_queue()
show_queue()

#ćw 7
#1
def anagram(text1,text2):
    '''Funkcja sprawdza, czy text1 i text2 są złożone z tych samych liter'''
    for w in text1:
        if w in text2:
            print('To jest anagram')
            return True
        else:
            print('To nie jest anagram')
            return False

anagram('ala','lal')
anagram('rower','julia')

#2
def pole_koła(r):
    '''Funkcja oblicza pole koła'''
    if r>0:
        print(int(math.pi * r ** 2))
    elif r<0 or r==0:
        raise ValueError('Podaj dodatni promień r.')
pole_koła(6)

#3
rr = random.randint(0, 100)
print(rr)
if rr > 2 and rr %2 != 0 and rr %3 != 0 and rr %5 != 0 and rr %7 != 0:
    print('Liczba jest liczbą pierwszą')
elif rr == 2 or rr == 3 or rr == 5 or rr == 7:
    print('Liczba jest liczbą pierwszą')
else:
    print('Nie jest liczbą pierwszą')


#ćw 8
#1
def word_with_a(napisy):
    '''Funkcja zwraca listę zawierjącą napisy z literą a'''
    return [napis for napis in napisy if 'a' in napis]

ww = ['ala', 'ada','rower']
print(word_with_a(ww))

#2
def kwadraty_liczb(liczby):
    kwadraty = [liczba for liczba in liczby if int(liczba ** 0.5) ** 2 == liczba and int(liczba ** 0.5) in liczby]
    return print(kwadraty)

lista_kw = [1,2,4,5]
kwadraty_liczb((lista_kw))

# 3
produkty = {'linijka': 20, 'kalkulator': 33, 'zeszyt': 5, 'monitor': 900}
ceny = list(produkty.values())
ceny.sort()
print(ceny[-1])


# ćw 9
# 1

class Książka():
    def __init__(self, tytuł, autor, rok_wydania):
        self.tytuł = tytuł
        self.autor = autor
        self.rok_wydania = rok_wydania

    def __str__(self):
        return f"Tytuł: {self.tytuł}, Autor: {self.autor}, Rok wydania: {self.rok_wydania}"

    def wydano_przed_2000(self):
        if self.rok_wydania < 2000:
            return True
        else:
            return False

book = Książka('Pan Tadeusz', 'Adam Mickiewicz', 1834)
print(book.wydano_przed_2000())


# 2

class Produkt():
    koszyk = []
    def __init__(self, nazwa, cena, ilość):
        self.nazwa, self.cena, self.ilość = nazwa, cena, ilość

    def __str__(self):
        return f"Nazwa produktu: {self.nazwa}, Cena: {self.cena}, Ilość: {self.ilość}"

    def dodanie_do_koszyka(self, artykuł, koszyk):
        if artykuł.nazwa == self.nazwa:
            self.ilość += artykuł.ilość
            print('Zwiększono ilość posiadanych artykułów')
        else:
            koszyk.append(artykuł)
            print('Dodano nowy artykuł do koszyka')

    def usuwanie_z_koszyka(self, artykuł, koszyk):
        if artykuł.nazwa == self.nazwa:
            self.ilość =- artykuł.ilość
            print('Zmniejszono ilość posiadanych artykułów')
        elif self.ilość == 0:
            print('W koszyku nie ma posiadanych artykułów')
        else:
            koszyk.pop(artykuł)
            print('Usunięto artykuł z koszyka')

    def liczba_artykułów(self, koszyk):
        return len(koszyk)

#3
class FiguraGeometryczna():
    pass

class Trójkąt(FiguraGeometryczna):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"A: {self.a}, B: {self.b}, C: {self.c}"

    def pole_trójkąta(self):
        '''Liczy pole na podstawie wzoru Herona'''
        if self.a + self.c > self.b and self.b + self.c > self.a and self.a + self.c > self.b:
            p = (self.a + self.b + self.c) / 2
            pole = math.sqrt(p *  (p - self.a) * (p - self.b) * (p - self.c))
            return f"Pole trójkąta o bokach {self.a}, {self.b}, {self.c} wynosi: {pole}."
        else:
            raise ValueError('Z podanych boków nie da się utworzyć trójkąta')

    def obwód_trójkąta(self):
        if self.a + self.c > self.b and self.b + self.c > self.a and self.a + self.c > self.b:
            o = self.a + self.b + self.c
            return f"Obwód trójkąta o bokach {self.a}, {self.b}, {self.c} wynosi: {o}."
        else:
            raise ValueError('Z podanych boków nie da się utworzyć trójkąta')


tr = Trójkąt(3,4,5)
print(tr)
print(tr.pole_trójkąta())
print(tr.obwód_trójkąta())

#4
class Pojazd():
    def __init__(self, marka, model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji

    def __str__(self):
        return f"Marka pojazdu: {self.marka}, model: {self.model}, rok_produkcji: {self.rok_produkcji}"

class Samochod(Pojazd):
    def __init__(self, marka, model, rok_produkcji, liczba_drzwi):
        self.liczba_drzwi = liczba_drzwi
    def __str__(self):
        return f"Liczba drzwi: {self.liczba_drzwi}"

class Motocykl(Pojazd):
    def __init__(self,marka, model, rok_produkcji, pojemnosc_silnika):
        self.pojemnosc_silnika = pojemnosc_silnika
    def __str__(self):
        return f"Pojemność silnika: {self.pojemnosc_silnika}"

moto = Motocykl("Yamaha", "MT-07", 2019,689)
auto = Samochod('Opel','Insignia',2015,5)
print(auto)
print(moto)

#ćw 10

#1
class Kwadrat():
    def __init__(self,a):
        self.a = a
    def oblicz_pole(self):
        if self.a>0:
            pole_kw = self.a**2
            return f"Pole kwadratu: {pole_kw}"
        else:
            raise ValueError('Bok kwadratu musi być dodatni')

class Koło():
    def __init__(self, r):
        self.r = r

    def oblicz_pole(self):
        if self.r > 0:
            pole_koła = int(math.pi * self.r**2)
            return f"Pole koła: {pole_koła}"
        else:
            raise ValueError('Promień koła musi być dodatni')

kwadrat = Kwadrat(3)
print(kwadrat.oblicz_pole())
kolo = Koło(5)
print(kolo.oblicz_pole())

#2
class Osoba():
    def __init__(self,imie,nazwisko,wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def __str__(self):
        return f"Imię: {self.imie}, nazwisko: {self.nazwisko}, wiek: {self.wiek}"

    @property
    def imie(self):
        return self.__imie

    @imie.setter
    def imie(self, imie):
        self.__imie = imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @nazwisko.setter
    def nazwisko(self, nazwisko):
        self.__nazwisko = nazwisko


new_person = Osoba('Julia','Tyrka',20)
print(new_person)
print(new_person.imie)

#3

class Zwierze():
    def __init__(self, imie):
        self.imie = imie

    @abstractmethod
    def daj_glos(self):
        pass

class Pies(Zwierze):
    def daj_glos(self):
        return f"{self.imie} szczeka"

class Kot(Zwierze):
     def daj_glos(self):
        return f"{self.imie} miauczy"

kot = Kot('Milusia')
pies = Pies('Diego')
print(kot.daj_glos())
print(pies.daj_glos())

#4
def mnoz_razy_2(f):
    def funkcja(*args, **kwargs):
        return f(*args, **kwargs) * 2
    return funkcja

@mnoz_razy_2
def dzialanie(x,y):
    return (x - y)+x

print(dzialanie(2,1))
