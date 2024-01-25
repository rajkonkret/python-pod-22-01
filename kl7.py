from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opsiująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print('Tu', self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")

    def wydaj_odglos(self):
        print("kokokokok")


class Orzel(Ptak):
    def poluj(self):
        print("Tu", self.gatunek, "rozpoczynam polowanie")

    def wydaj_odglos(self):
        print("Kier kieeer kir")


class Sowa(Ptak):
    """
    Klasa Sowa
    nie nadpisuje metody wydaj_odglos - musi nadpisac bo metoda jest abstrakcyjna
    """


#     or1 = Ptak("Orzel Bielik", 45)
#           ^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzel Bielik", 45)
# or1.latam()  # Tu Orzel Bielik Lecę z szybkością 45
# or1.wydaj_odglos()

# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam
kur2.dziobanie()
kur2.wydaj_odglos()

or2 = Orzel("Orzeł bielik", 60)
or2.latam()
or2.poluj()  # Tu Orzeł bielik rozpoczynam polowanie
or2.wydaj_odglos()
# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# sow = Sowa()
