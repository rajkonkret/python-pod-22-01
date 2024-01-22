wiek = 47
rok = 2023
temp = 36.6  # float
# x = 36,6 - to nie jest liczba!

print(temp)
print(type(temp))  # <class 'float'>

print(5 * "Radek")  # RadekRadekRadekRadekRadek

print(wiek * rok)
print(wiek + rok)
print(wiek - rok)
print(wiek / rok)  # wynik float
# 95081
# 2070
# -1976
# 0.023232822540781017
print(wiek // rok)  # 0 - czesc całkowita z dzielenie
print(wiek % rok)  # modulo - reszta z dzielenia
# 5 5 2 = 2 r 1

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
wynik = 0.2 + 0.7
print(wynik)
print(f"{wynik:.2f}")
# 0.8999999999999999
# 0.90
print(f"sprawdzenie zmiennej {temp} {wiek}")  # sprawdzenie zmiennej 36.6 47

print(f"""
Sprawdzzennie
zmiennej
{temp}
{wiek
}""")

# typ logiczny
# True, False
print(type(True))  # <class 'bool'>
print(type(False))  # <class 'bool'>

print(int(True))  # 1
print(int(False))  # 0
print(bool(1))  # True
print(bool(100))  # True
print(bool(-10))  # True
print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # False odpowiednik null

a = 14
b = 3
print(f"Wynik porównania {a} > {b} = {a > b}")
print(f"Wynik porównania {a} < {b} = {a < b}")
print(f"Wynik porównania {a} == {b} = {a == b}")  # == - porównanie
print(f"Wynik porównania {a} != {b} = {a != b}")  # != różne
print(f"Wynik porównania {a} >= {b} = {a >= b}")
print(f"Wynik porównania {a} <= {b} = {a <= b}")
# Wynik porównania 14 > 3 = True
# Wynik porównania 14 < 3 = False
# Wynik porównania 14 == 3 = False
# Wynik porównania 14 != 3 = True
# Wynik porównania 14 >= 3 = True
# Wynik porównania 14 <= 3 = False
