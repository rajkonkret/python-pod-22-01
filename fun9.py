# funkcja lambda
# skrócona forma funkcji
# mozliwosc wykonania w miejscu deklaracji
# funkcja anonimowa
from functools import reduce


def odejmij2(a, b):
    return a - b


print(odejmij2(8, 12))

odejmij = lambda a, b: a - b  # lambda zwraca wynik (return)

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))
print(wiek(10))
print(wiek(18))
print(wiek(25))

lista = [1, 2, 3, 4, 24, 45, 50, 100, 200]

l = []
for i in lista:
    l.append(i * 2)

print(l)  # [2, 4, 6, 8, 48, 90, 100, 200, 400]
print([i * 2 for i in lista])  # [2, 4, 6, 8, 48, 90, 100, 200, 400]


# map()  - bierze kolejne elementy i zmienia wg zadanej funkcji

def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))

print(l2)  # [2, 4, 6, 8, 48, 90, 100, 200, 400]

print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 48, 90, 100, 200, 400]
# użycie lambdy jako funkcji anonimowej, wykonanie w miejscu deklaracji
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")

# filtrowanie danych
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)

print(l3)

# filter()
print(f'Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}')
# Zastosowanie filter(): [1, 2]
# x > 20
lista_filter = list(filter(lambda x: x < 3, lista))
print(lista_filter)  # [1, 2]

# x wieksze do 3 i mniejsze od 50
print(f'Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 50, lista))}')
print(f'Zastosowanie filter(): {list(filter(lambda x: 3 < x < 50, lista))}')
# Zastosowanie filter(): [4, 24, 45]
# Zastosowanie filter(): [4, 24, 45]

# reduce()
lista_reduce = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, lista_reduce))  # 15
# 1 + 0 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
