# set - zbiór - przechowuje unikalne wartości
# nie zachowuje kolejnosci przy dodawaniu elemnetów do listy
# w zbiorze nie ma indeksu
lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # zamiana na set
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

zb2 = set()  # tworzenie pustego zbioru
print(zb2)  # set()  wyswietlenie pustego zbioru

zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

# usuniecie elementu - zwraca usuniety, usunie pierwszy
print(zbior.pop())  # 33

# usunięcie po elemencie
zbior.remove(55)
print(zbior)  # {66, 777, 11, 44, 18, 22}

zbior_copy = zbior.copy()  # kopia elementów zbioru
print(zbior_copy)  # {66, 18, 22, 777, 11, 44}  zmieniona kolejność

zbior2 = {667, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {18, 52, 999, 11, 44, 667, 62}

print(zbior | zbior2)  # suma zbiorów {66, 999, 777, 11, 44, 18, 52, 22, 667, 62}
print(zbior & zbior2)  # częśc wspólna   {18, 11, 44}
print(zbior - zbior2)  # róznica {777, 66, 22}
print(zbior.difference(zbior2))  # {777, 66, 22}
print(zbior.union(zbior2))  # {66, 999, 777, 11, 44, 18, 52, 22, 667, 62}
print(zbior.update(zbior2))  # None nie daje nowego zbioru
# zmienia bazowy zbior
print(zbior)  # {66, 999, 777, 11, 44, 18, 52, 22, 667, 62}
