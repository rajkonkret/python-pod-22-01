# krotka - niezmienna kolekcja
# efektywniej wykorzystuje zasoby komputera


tupla1 = "Radek"  # str
tupla2 = ("radek")
print(type(tupla2))  # <class 'str'>
tupla3 = "radek",
print(type(tupla3))  # <class 'tuple'>
tupla4 = ("radek",)
print(type(tupla4))  # <class 'tuple'>
print(tupla4)  # ('radek',)
tupla5 = "radek", "tomek", "marek", 'Tadek'
print(type(tupla5))  # <class 'tuple'>
temp = 36, 6
print(type(temp))  # <class 'tuple'>
tupla_liczba = 43, 55, 22.34, 11, 200
print(type(tupla_liczba))
print(tupla_liczba)  # (43, 55, 22.34, 11, 200)

# temp[0] = 1  # TypeError: 'tuple' object does not support item assignment

# del
# del temp[0]  # usuniecie elemntu z tupli  TypeError: 'tuple' object doesn't support item deletion

# mozna usunac cała tuple
del temp
# print(temp)  # NameError: name 'temp' is not defined

print(tupla_liczba[0])
print(tupla_liczba[0:3])  # (43, 55, 22.34) 0,1,2
print("radek" in tupla5)  # True
print(tupla5.index("radek"))
print(tupla5.count("radek"))

print(sorted(tupla5))  # ['Tadek', 'marek', 'radek', 'tomek'] - dostalismy liste

# rozpakowanie tupli
a, b = 1, 2
print(a)
print(b)

# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3  # * - worek na dane
print(a)
print(b)  # [2, 3]

# * moze byc przy jednej zmiennej
*imie1, imie2, imie3 = tupla5
print(imie1, imie2, imie3)
imie1, *imie2, imie3 = tupla5
print(imie1, imie2, imie3)
imie1, imie2, *imie3 = tupla5
print(imie1, imie2, imie3)
# ['radek', 'tomek'] marek Tadek
# radek ['tomek', 'marek'] Tadek
# radek tomek ['marek', 'Tadek']

lista_tupla = list(tupla5)
print(type(lista_tupla))  # <class 'list'>
print(lista_tupla)  # ['radek', 'tomek', 'marek', 'Tadek']
