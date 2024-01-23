# for - petla iteracyjna
import random
from pprint import pprint
from itertools import zip_longest

for i in range(5):  # 0..4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # niema zmienna
    pass
    # print(_)

for i in range(10):
    print(i * 2)

#
lista_kula = list(range(1, 50))  # 1..49

lista_wylosowane = []
for i in range(6):
    wyn = random.choice(lista_kula)
    lista_kula.remove(wyn)
    print(wyn)
    lista_wylosowane.append(wyn)

print(lista_wylosowane)
pprint(lista_kula)

for i in range(10):
    if i % 2 == 0:
        print(i, "jest parzysta")

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)

for c in lista_wylosowane:
    if c > 10:
        print("wieksze od 10")
    print(c)

for i in range(0, 10, 2):  # start, stop, krok 0..9 krok 2
    print(i)

for i in range(-10, 0, 2):
    print(i)

for i in range(10, 0, -2):  # krok ujemny, liczy do tyłu
    print(i)

for c in lista3:
    if c == 2:
        c += 1  # c= c+ 1
    print(c)

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

imiona = ['Radek', "Tomek", 'Zenek', 'Ania']
print(imiona)
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)

# wyswietlic elemnty z listy w postaci:
# 0 Radek

for i in range(len(imiona)):  # range(4) 0..3
    print(i, imiona[i])

for p in imiona:
    print(imiona.index(p), p)

# enumerate() - numeruje elemnty kolekcji
for p in enumerate(imiona):
    print(p)  # (3, 'Ania')

# rozpakowanie krotki i,p = (3, 'Ania')
for i, p in enumerate(imiona):
    print(i, p)

for i, p in enumerate(imiona, start=1):
    print(i, p)  # 1 Radek

# ludzie = ['Radek', 'Janek', 'Asia', 'Tadek']
ludzie = ['Radek', 'Janek', 'Asia', 'Tadek', 'Marek']  # przy for IndexError: list index out of range

wiek = [44, 55, 23, 32]
# wyswietlic w postaci Radek 44
#
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])

# zip() - łaczenie kolekcji
for i in zip(ludzie, wiek):
    print(i)  # ('Radek', 44)

for p, w in zip(ludzie, wiek):
    print(p, w)  # Janek 55

# wyswietlic w postaci 0 Radek 44
for i in enumerate(zip(ludzie, wiek)):
    print(i)  # (3, ('Tadek', 32))
a, b = (3, ('Tadek', 32))
# a -> 3
# b -> ('Tadek', 32)
# c,d = b
# c -> 'Tadek'
# d -> 32
# a,(c,d)

for i, (p, w) in enumerate(zip(ludzie, wiek)):
    print(i, p, w)
# 0 Radek 44
# 1 Janek 55
# 2 Asia 23
# 3 Tadek 32

zipped = zip_longest(ludzie, wiek, fillvalue=None)
print(zipped)  # <itertools.zip_longest object at 0x0000019E03380AE0>
# for zipp in zipped:
#     print(zipp)
# poniewaz zipped jest typu iterator musimy zapamietac sobie elemnty w innej kolekcji by móc używac wielokrotnie
zip_list = list(zipped)
for item in zip_list:
    print(item)
# ('Radek', 44)
# ('Janek', 55)
# ('Asia', 23)
# ('Tadek', 32)
# ('Marek', None)
print("-------------")
# for zipp in zipped:
#     print(zipp)
for item in zip_list:
    print(item)  # ('Radek', 44)

for i, w in zip_list:
    print(i, w)  # Marek None
