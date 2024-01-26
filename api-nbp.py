import requests as re

url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'

response = re.get(url)
print(response.text)
data = response.json()
print(data)
