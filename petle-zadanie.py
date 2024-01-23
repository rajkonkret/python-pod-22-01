# napisac aplikacje kalkulator
# z wykorzystaniem petli while
# przechwycic wyjatki
# dodac mozliwosc wyjscia z programu
#
# wyswitlic menu  z dostepnymi operacjami
# po wybraniu operacji pobrac a i b
# wyswietlic wynik w zależnosci od wybranej operacji
# Wynik dzielenia 8 / 4 = 2
while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podaj działanie do wykonania")

    if odp == "5":
        break
    try:
        a = int(input("Podaj pierwszą liczbę"))
        b = int(input("Podaj drugą liczbę"))

        if odp == "1":
            print(f"Wynik dodawnia {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Wynik dodawnia {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Wynik dodawnia {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Wynik dodawnia {a} / {b} = {a / b}")
    except ZeroDivisionError:
        print("Dzielenie przez zero!!!")
    except (TypeError, ValueError):
        print("Błąd wartości i typu")
    except Exception as e:
        print("Błąd", e)
    else:
        print("Obliczenia wykonane poprawnie")
    finally:
        print('Wykona się zawsze')
