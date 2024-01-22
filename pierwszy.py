import sys

print()  # wydrukuj/wypisz - pusta linia
print("Nazywam się Radek")
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radekk')
print('Nazywam się Radekk')
# ctrl d - powielanie elmentu
# ctrl z - cofnij
print(type("Radek"))  # <class 'str'> - typ tekstowy
# type() - sprawdzenie typu
print("39" + "14")  # 3914 konkatenacja tekstow - łączenie
print(39)
print(type(39))  # <class 'int'> liczby całkowite
# print(39 + "14")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# nie wie jaki wariant wybrac
print("39" + "14")
print(39 + 14)
print(int("39") + 56)  # int() - rzutowanie na int (zamiana)
print(str(39) + "14")  # str() - rzutowanie na str - konkatenacja stringów
# typowanie dynamiczne
# silne typowanie - nie zamienia typow podczas wykonywania obliczen, musimy jawnie wskazac
print(5 * "4")  # 44444
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)

# zmienna - pudelko na dane
# snake_case

name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>
name = 67
print(name)
print(type(name))  # <class 'int'>
name: str = 90
print(type(name))  # <class 'int'>

age = 48
print(age)
print(type(age))
