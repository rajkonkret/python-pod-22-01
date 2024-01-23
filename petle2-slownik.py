dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}
print(type(dictionary))  # <class 'dict'>

#  wypisanie kluczy ze słownika
for i in dictionary.keys():
    print(i)
# imie
# nazwisko

for i in dictionary:
    print(i)
# imie
# nazwisko

# wypisanie wartosci
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisanie par
for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski
# """
#    Prints the values to a stream, or to sys.stdout by default.
#
#      sep
#        string inserted between values, default a space.
#      end
#        string appended after the last value, default a newline.
#      file
#        a file-like object (stream); defaults to the current sys.stdout.
#      flush
#        whether to forcibly flush the stream.
#    """
print("Radek", end='')
print("Tomek")  # RadekTomek  tu znak konca lini \n
print("Nastepny")  # Nastepny

dictionary2 = {'name': 'imie', 'company': "Lidl"}
d = {}
for k, v in dictionary2.items():
    d[v] = k

print(d)  # {'imie': 'name', 'Lidl': 'company'}
print({value: key for key, value in dictionary2.items()})
