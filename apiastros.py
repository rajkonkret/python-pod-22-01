import requests

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)
print(response)
# <Response [200]>
# 3xx przekierowania
# 4xx - błedy klienta 404 błedny url, 400 Bad Request błedne zapytanie
# 5xx - błedy serwera
print(response.text)  # odczytanie jsona  zbody odpowiedzi

response_json = response.json()  # zamienia jsona na słownik
print(response_json)
print(type(response_json))  # <class 'dict'>

print(response_json.keys())
# dict_keys(['message', 'people', 'number'])
people = response_json['people']
print(people)
# [{'name': 'Jasmin Moghbeli', 'craft': 'ISS'}, {'name': 'Andreas Mogensen', 'craft': 'ISS'},
#  {'name': 'Satoshi Furukawa', 'craft': 'ISS'}, {'name': 'Konstantin Borisov', 'craft': 'ISS'},
#  {'name': 'Oleg Kononenko', 'craft': 'ISS'}, {'name': 'Nikolai Chub', 'craft': 'ISS'},
#  {'name': "Loral O'Hara", 'craft': 'ISS'}]
for p in people:
    print(p['name'])
# Jasmin Moghbeli
# Andreas Mogensen
# Satoshi Furukawa
# Konstantin Borisov
# Oleg Kononenko
# Nikolai Chub
# Loral O'Hara
