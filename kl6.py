# klasa Pracownik, metoda przedstaw_sie, oblicz_pensje
# klasa Kierownik - dziedziczy po Pracownik
class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Kierownik(Pracownik):
    """
    Kierownik
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 100000)
pracownik.przedstaw_sie()
pensja_prac = pracownik.oblicz_pensje()
print(f"Wynagrodzenie dla pracownika: {pracownik.imie} {pracownik.nazwisko}: {pensja_prac}")
# Cześć, jestem Jan Kowalski
# Wynagrodzenie dla pracownika: Jan Kowalski: 100000

kierownik = Kierownik("Anna", "Nowak", 50000, 5)
kierownik.przedstaw_sie()
pensja_kier = kierownik.oblicz_pensje()
print(f"Wynagrodzenie dla kierownika: {kierownik.imie} {kierownik.nazwisko}: {pensja_kier}")
