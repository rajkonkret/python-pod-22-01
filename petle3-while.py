# while - sterowana warunkiem

licznik = 0
while True:
    licznik += 1
    print('Komunikat!!!')
    if licznik > 10:
        break

print(licznik)
licznik = 0
while licznik < 10:
    print('Komunikat2 !! !! !!')
    licznik += 1

# password = input('Podaj hasło')
# while password != 'secret':
#     password = input("Błędne hasło. podaj ponownie")
# print("Hasło prawidłowe")

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)
print(lista_int)
