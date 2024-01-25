class Human:
    """
    Klasa human opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca - konstruktor
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywma się {self.imie}")

    def podaj_wiek(self):
        print(f"Mój wiek {self.wiek}")

    def podaj_wzrost(self):
        print(f"Mój wzrost {self.wzrost}")

    def podaj_plec(self):
        print(f"Jestem {self.plec}")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")

    def __repr__(self):  # reprezentacja obiektu
        return f'{self.imie}, {self.wiek}'


# cz1 = Human()
# print(cz1)  # <__main__.Human object at 0x0000017466085E80>
# cz1.imie = "Radek"
# print(cz1.imie)

cz1 = Human("Ania", 35, 170)
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)

cz2 = Human(imie="Radek", wiek=67, wzrost=193, plec="m")
print(cz2.imie)
cz1.podaj_wiek()
cz1.podaj_wzrost()
cz1.powitanie()
cz1.podaj_plec()
cz1.ruszaj()
cz2.ruszaj()
# Nazywma się Ania
# Jestem k
# Ruszyłam w drogę
# Ruszyłem w drogę

lista = [cz1, cz2]
for i in lista:
    print(i.imie)

# Ania
# Radek
print(cz1)  # <__main__.Human object at 0x0000029C5FE07440>
# po nadpisaniu metody __repr__
# Ania, 35
