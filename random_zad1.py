import random  # biblioteka do losowania liczb pseudolosowych

print(random)
# <module 'random' from 'C:\\Program Files\\Python312\\Lib\\random.py'>

# help(random)

print(random.randint(1, 100))  # int between 1 and 100
print(random.random())  # float between 0.0 and 0.999999
print(random.random() * 10)  # float between 0.0 and 9.99999
print(random.randrange(7))  # int between 0 and 6
print(random.randrange(1, 100))  # int between 1 and 99

lista = [1, 2, 3, 45, 57, 68, 79]
print(random.choice(lista))

lista_kula = list(range(1, 50))  # 1..49

wyn = random.choice(lista_kula)
lista_kula.remove(wyn)
print(wyn)
wyn = random.choice(lista_kula)
lista_kula.remove(wyn)
print(wyn)
wyn = random.choice(lista_kula)
lista_kula.remove(wyn)
print(wyn)
wyn = random.choice(lista_kula)
lista_kula.remove(wyn)
print(wyn)
wyn = random.choice(lista_kula)
lista_kula.remove(wyn)
print(wyn)
wyn = random.choice(lista_kula)
lista_kula.remove(wyn)
print(wyn)

print(random.choices(lista_kula, k=6))  # losuje powtarzajce się liczby [47, 18, 7, 46, 46, 40]
print(random.sample(lista_kula, 6))  # losuje bez powtórzeń [20, 33, 39, 30, 44, 38]
print(random.sample(lista_kula, k=6))  # losuje bez powtórzeń [1, 19, 28, 11, 14, 43]
