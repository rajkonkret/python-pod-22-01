class Car:
    """
    Klasa opisująca samochód  w Pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # pole prywatne

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):
        print('Zmiana biegu')


ca1 = Car("Elektryczny", 2024)
ca1.gaz()
ca1.gaz()
ca1.gaz()
ca1.gaz()
ca1.gaz()
# print(ca1.__predkosc)  # 50, AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
ca1.licznik()  # Prędkość wynosi 50 km/h
ca1.__predkosc = 0
ca1.licznik()  # Prędkość wynosi 50 km/h
ca1.hamuj()
ca1.hamuj()
ca1.hamuj()
ca1.hamuj()
ca1.hamuj()
ca1.licznik()  # Prędkość wynosi 0 km/h
