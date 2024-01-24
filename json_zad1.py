# typ json - dane typu para klucz-wartość
# json => {"name" : "Radek"}

import json

print_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(print_dict))  # <class 'dict'>

with open('nasze_dane.json', 'w') as f:
    json.dump(print_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}
# upiekszanie
with open('nasze_dane.json', 'w') as f:
    json.dump(print_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }
# sortowanie po kluczach
with open('nasze_dane.json', 'w') as f:
    json.dump(print_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

# odczyt jsona do słownika
with open('nasze_dane.json', "r") as fh:
    data = json.load(fh)

print(data)
print(type(data))
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
# <class 'dict'>
print(data.get('name'))
print(data['name'])
# Radek
# Radek

json_text = json.dumps(data, indent=4, sort_keys=True)
print(json_text)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

dict_json = json.loads(json_text)
print(dict_json)
print(type(dict_json))
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
# <class 'dict'>
