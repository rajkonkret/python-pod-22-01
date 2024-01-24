# napisac funkcje obliczjąca średnią
def liczby(imie=None, *cyfry):
    print(cyfry)  # () - krotka
    suma = 0
    count = len(cyfry)
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Błąd", e)
    else:
        print(f'{imie}: średnia wynosi {avg}')
    finally:
        print("Koniec")


liczby()
liczby(1, 2, 3, 4, 5)
liczby(100, 300, 400, 500, 1, 345, 23)
liczby("Radek", 1, 2, 3, 4, 5)  # Błąd unsupported operand type(s) for +=: 'int' and 'str'
a, *cyfry = "Radek", 1, 2, 3, 4, 5
