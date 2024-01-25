# zrobic klase Dom
# metraz, kolor, liczba_okien
# zrobic pola prywatne
# wystawic metody do odczytu i zapisu tych pol
# dodac metode prywatna farba() - napis zabrakło farby w kolorze..... wywołana w zmien_kolor
class Dom:
    """
    Klasa opisująca Dom
    """

    def ___init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_koien = liczba_okien

    def mam_kolor(self):
        print(f"Mam kolor {self.__kolor}")

    def mam_metraz(self):
        print(f"Mam metraz {self.__metraz}")

    def mam_liczba_okien(self):
        print(f"Mam okien {self.__liczba_koien}")

    def zmien_kolor(self):
        wybor = input("Podaj nowy kolor")
        self.__kolor = wybor
        self.__farba()

    def zmien_metraz(self):
        wybor = int(input("Podaj nowy metraz"))
        self.__metraz = wybor

    def zmien_liczba_okien(self):
        wybor = int(input("Podaj nowa liczbę okien"))
        self.__liczba_koien = wybor

    def __farba(self):
        print("Zabrakło farby")
