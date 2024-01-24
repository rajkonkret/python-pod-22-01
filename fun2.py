# funkcje zwracające wynik
# return

def dodaj(a, b):
    """
    funkcja oblicza a + b
    :param a:
    :param b:
    :return: wynik dodawania
    """
    return a + b  # return - zwróć wynik


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj.__doc__)

# funkcja
# oblicza
# a + b
# :param
# a:
# :param
# b:
# :return: wynik
# dodawania


print(dodaj(5, 6))  # 11
wyn = dodaj(7, 9)
print(f'wynik działania {wyn}')  # wynik działania 16

print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=15, cena=1000))

zm = oblicz_vat(1000)
print(zm)
print(type(zm))  # <class 'float'>

if zm == 1230:
    print("OK")
