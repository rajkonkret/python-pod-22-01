# słownik - para klucz wartosc
# {'name' :'Radek'}
# odpowiedni9k jsona
# klucze ni emoga sie powtarzać

dictionary = dict()
print(dictionary)  # {} pusty słownik
dictionary1 = {}  # pusty słownik
print(dictionary1)  # {}

dictionary['imie'] = 'Radek'
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 39
print(dictionary)  # {'imie': 'Radek', 'wiek': 39}

dictionary['imie'] = "Tomek"
print(dictionary)  # ponowne dodanie klucza istniejacego zmienia wartość dla twgo klucza {'imie': 'Tomek', 'wiek': 39}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Tomek', 39])
# dict_items([('imie', 'Tomek'), ('wiek', 39)])

dictionary.update({'date': '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 39, 'date': '12-12-2024'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 4)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 4}

word = input("Podaj słowko")
print(word)

# aplikcja slownik
# pobrac słowo i przetłumaczyc
#
# aplikacja kalkulator
# pobrac a i b
# wypisac wynik np.: dodawania
print(2024 ** 47)
print(len(str(2024 ** 47)))  # 156

print(dictionary['imie'])  # Tomek
# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary.get('imie'))  # Tomek
print(dictionary.get('Imie', 'default'))  # default

dict_pol_eng = {'imie': 'name', 'cat': 'kot', 'drzewo': 'tree'}
print(f"Mamy w słowniku {dict_pol_eng.keys()}")
odp = input('Podaj słówko do przetłumaczenia')
print(dict_pol_eng[odp.replace(" ", "").lower()])

# input zwraca stringa, musimy zadbac o to by robic działania na liczbach
a = float(input('podaj pierwsza liczbe'))
b = input('podaj drugą liczbe')
print(a + int(b))
