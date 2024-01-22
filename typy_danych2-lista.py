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