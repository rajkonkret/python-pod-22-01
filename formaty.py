import sys

user = "Tomek"  # str
wiek = 30  # int
wersja = 3.90001  # zmiennoprzecinkowe float
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
liczba = 134567234890  # int
print("Witaj %s masz teraz %d lat" % (user, wiek))  # Witaj Tomek masz teraz 30 lat
# TypeError: %d format: a real number is required, not str
# print("Witaj %d masz teraz %s lat" % (user, wiek))  # Witaj Tomek masz teraz 30 lat
# %s string
# %d digit - liczba
print("Witaj %(user)s, masz teraz %(age)d lat" % {'user': user, "age": wiek})
# TypeError: %d format: a real number is required, not str
# print("Witaj %(user)d, masz teraz %(age)d lat" % {'user' : user, "age" : wiek})

print("Witaj {}, masz teraz {} lat".format(user, wiek))  # Witaj Tomek, masz teraz 30 lat
print(f'Witaj {user}, masz teraz {wiek} lat.')
print(f'Witaj {user}, masz teraz {wiek} lat.'.upper())  # WITAJ TOMEK, MASZ TERAZ 30 LAT.

print("Uzywamy wersji Python %i" % 3)  # Uzywamy wersji Python 3
print("Uzywamy wersji Python %f" % 3)  # Uzywamy wersji Python 3.000000
print("Uzywamy wersji Python %f" % 3.9)  # Uzywamy wersji Python 3.900000
print("Uzywamy wersji Python %.1f" % 3.9)  # Uzywamy wersji Python 3.9
print("Uzywamy wersji Python %.2f" % 3.9)  # Uzywamy wersji Python 3.90
print("Uzywamy wersji Python %.0f" % 3.9)  # Uzywamy wersji Python 4
print("Uzywamy wersji Python %.f" % 3.9)  # Uzywamy wersji Python 4
# zaokrągla przy wyswietlaniu
a = 3.14
b = round(a)
print(a, b)  # 3.14 3
c = round(a, 1)
print(c)  # 3.1

print(f"Uzywamy wersji Python {wersja}")
print(f"Uzywamy wersji Python {wersja:.1f}")
print(f"Uzywamy wersji Python {wersja:.2f}")
print(f"Uzywamy wersji Python {wersja:.0f}")
# Uzywamy wersji Python 3.9
# Uzywamy wersji Python 3.90
# Uzywamy wersji Python 4
# alt shift insert - column selection
print(f"{user:>10}")  # "     Tomek"
print(f"{user:<20}")  # "Tomek               "
print(f"{user:^20}")  # "      Tomek        "

print(liczba)  # 134567234890
print('Nasza duża liczba {:,}'.format(liczba))  # Nasza duża liczba 134,567,234,890
print('Nasza duża liczba {:,}'.format(liczba).replace(",", "."))  # Nasza duża liczba 134.567.234.890
print('Nasza duża liczba {:,}'.format(liczba).replace(",", " "))  # Nasza duża liczba 134 567 234 890
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 134,567,234,890
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 134 567 234 890
liczba2 = 112345.786
print(f"Nasza duża liczba {liczba2:,}")  # Nasza duża liczba 112,345.786
