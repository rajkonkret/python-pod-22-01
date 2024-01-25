# klasa  - szablon, przepis wg jakiego ma byc zbudowany obiekt
# cechy - pola
# funkcje - funkcje mozliwe do wykonania np.: na obiektach
# obiekt - stworzony wg przepisu (instancja)

class Human:
    """
    klasa Human opisująca człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywma się {self.imie}")

    def podaj_wiek(self):
        print(f"Mam {self.wiek} lat")


print(Human.__doc__)  # klasa Human opisująca człowieka w Pythonie
cz1 = Human()  # tworzenie obiektu klasy Human (instancji)

print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)
"""
    
k
None
"""
cz1.imie = "Magda"
print(cz1.imie)  # Magda
print(type(cz1))  # <class '__main__.Human'>
cz1.wiek = 24
print(cz1.wiek)

cz2 = Human()
cz2.imie = "Radek"
cz2.wiek = 79
cz2.plec = "m"

print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
cz1.powitanie()
cz2.powitanie()
# Nazywma się Magda
# Nazywma się Radek
cz1.podaj_wiek()
cz2.podaj_wiek()
# Mam 24 lat
# Mam 79 lat
