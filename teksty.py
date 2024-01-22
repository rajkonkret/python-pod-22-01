tekst = "Witaj świecie"

print(tekst)
print(type(tekst))
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj świecie
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE
# ctrl lewy klawisz myszy na funkcji - wywołanie dokumentacji funkcji
# teksty w pythonie są immutable (niezmienne)
#         """ Return a copy of the string converted to uppercase. """
print(tekst.lower())
print(tekst.capitalize())
tekst_lower = tekst.lower()
print(tekst_lower)

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))  # "Witaj "

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie

print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))
print(tekst.count("j", 0, 4))  # 0
# indeks 0 - poczatek, indeks 4 koniec(niewłącznie)
# "Radek"

#  01234 -> 0,4 -> Rade R - 0 e - 3

imie = "Radek"
print(imie)
print("Imie:", imie)
starszy = "Witaj %s!"  # Imie: Radek
print(starszy % imie)  # Witaj Radek!

tekst_format = f"\tMam na imię {imie}\n i lubię Pythona.\b"
print(tekst_format)
print("\tMam na imię {}\n i lubię Pythona.\b".format(imie))
# "	Mam na imię Radek
#  i lubię Pythona"
# f - f-string odpowiednik format
print("Witaj {}!".format(imie))  # Witaj Radek!
print("""
    Tekst 
wielolinijkowy""")
#     Tekst
# wielolinijkowy

"""Komentarz wielolinijkowy"""
