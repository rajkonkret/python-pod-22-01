# lista - kolekcja przechowujaca dane
# moze przechowywac rózne typy w jedej liscie
# zapamiętuje kolejnosc przy dodawaniu elementów

lista = []  # pusta lista
print(type(lista))  # <class 'list'>
print(lista)  # []

lista.append("Radek")
lista.append("Tomek")
lista.append("Marek")
lista.append("Zenek")
lista.append("Maciek")
lista.append("Ala")
print(lista)  # ['Radek', 'Tomek', 'Marek', 'Zenek', 'Maciek', 'Ala']
print(lista[0])
print(lista[1])
# print(lista[10])  # IndexError: list index out of range
print(len(lista))  # len() długosc kolekcji
print(lista[-1])
print(lista[-2])

# slice
print(lista[0:3])  # ['Radek', 'Tomek', 'Marek'] 0,1,2
print(lista[-2:0])  # []
print(lista[-2:])  # ['Maciek', 'Ala']
print(lista[3:10])  # ['Zenek', 'Maciek', 'Ala']
print(lista[1::-1])  # ['Tomek', 'Radek']
print(lista[-2:0:-1])  # ['Maciek', 'Zenek', 'Marek', 'Tomek']

# nadpisanie elemntu
lista[2] = 'Mikołaj'
print(lista)  # ['Radek', 'Tomek', 'Mikołaj', 'Zenek', 'Maciek', 'Ala']

# wstawic element pomiędzy inne
lista.insert(1, "Martyna")
print(lista)
# ['Radek', 'Martyna', 'Tomek', 'Mikołaj', 'Zenek', 'Maciek', 'Ala']


# usnięcie elemntu z listy
lista.remove('Maciek')
print(lista)  # ['Radek', 'Martyna', 'Tomek', 'Mikołaj', 'Zenek', 'Ala']

indeks = lista.index("Ala")
print(indeks)

# usunięcie elemntu z listy po indeksie
print(lista.pop(indeks))  # Ala
print(lista)  # ['Radek', 'Martyna', 'Tomek', 'Mikołaj', 'Zenek']
lista.append("Radek")
print(lista)  # ['Radek', 'Martyna', 'Tomek', 'Mikołaj', 'Zenek', 'Radek']
lista.remove("Radek")
print(lista)  # ['Martyna', 'Tomek', 'Mikołaj', 'Zenek', 'Radek']

print("Radek" in lista)  # True

a = 6
b = 7
a = b
print(a)
print(b)
b = 8
print(a)

lista1 = lista  # kopiowanie referencji, adresu w pamieci
print(lista1)
print(lista)
lista_copy = lista.copy()  # kopiowanie elementów listy
lista.clear()  # usuniecie elemntów z listy
print(lista1)  # []
print(lista)  # []
print(lista_copy)  # ['Martyna', 'Tomek', 'Mikołaj', 'Zenek', 'Radek']
print(id(lista))  # 2089808613760
print(id(lista1))  # 2089808613760
print(id(lista_copy))  # 2089811445696

liczby = [54, 999, 34, 22.14, 687]
# liczby = [54, 999, 34, 22.14, 687, "A"]  # TypeError: '<' not supported between instances of 'str' and 'int'
print(type(liczby))  # <class 'list'>
liczby.sort()  # sortowanie listy
print(liczby)  # [22.14, 34, 54, 687, 999]

lista_osoby = ['Radek', 'Ola']
lista_osoby.sort()
print(lista_osoby)  # ['Ola', 'Radek']

liczby.reverse()  # odwraca kolejnosc
print(liczby)
liczby.sort(reverse=True)  # sortuje i odwraca kolejnosc
print(liczby)  # [999, 687, 54, 34, 22.14]

liczby.append(18)
liczby.remove(54)
print(liczby.pop(0))  # 999
print(liczby)  # [687, 34, 22.14, 18]
print(liczby.pop())  # 18 w liscie usunie ostatni element

# łączenie list
liczby3 = [88, 78, 34, 22, 11]
print(liczby + liczby3)  # [687, 34, 22.14, 88, 78, 34, 22, 11]

liczby.append(liczby3)
print(liczby)

liczby4 = [1, 2, 3, 4, 5]
liczby5 = [6, 7, 8, 9]
liczby5.extend(liczby4)
print(liczby5)  # [6, 7, 8, 9, 1, 2, 3, 4, 5]

tekst = "Python"
lista_str = list(tekst)  # zamienia na liste
print(lista_str)  # ['P', 'y', 't', 'h', 'o', 'n'] rozpakowanie sekwencji

lista_str2 = [tekst]  # tworzy i dodaje element do listy
print(lista_str2)  # ['Python']

# zamiana listy na krotke(tuple)
krotka = tuple(liczby)
print(krotka)  # (687, 34, 22.14, [88, 78, 34, 22, 11])
print(type(krotka))  # <class 'tuple'>
