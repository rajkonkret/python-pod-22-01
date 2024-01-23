# wyjatki - obsługa i rzucanie
# gdy wystapi bład python rzuca wyjątek
# my powinnismy przechwycic i obsłużyc wyjątek

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\python-pod-22-01\wyjatki.py", line 5, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

try:
    # print(5 / "00")
    # print(5 / 0)
    wynik = 5 / 1
except ZeroDivisionError:
    print("Błąd dzielenia przez 0")
except Exception as e:
    print("Błąd", e)
else:  # wykona się gdy nie ma błedu
    print('wynik', wynik)
finally:
    print("Zawsze")

print("Program nadal działa")
# Błąd dzielenia przez 0
# Program nadal działa
# Błąd unsupported operand type(s) for /: 'int' and 'str'
# Program nadal działa
# try - except [else-finally]
