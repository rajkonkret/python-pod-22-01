# dziedziczenie
class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):  # dziedziczy po klasie Pojazd
    """Klasa Samochod"""
    def __init__(self, kolor, marka):
        super().__init__(kolor)
        self.marka = marka

poj = Pojazd("Czerwony")
poj.info()

sam1 = Samochod("Zielony")
sam1.info()  # Kolor: Zielony

