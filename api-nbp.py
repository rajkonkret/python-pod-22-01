import requests as re

# url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'
url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'

response = re.get(url)
print(response.text)
data = response.json()
print(data)

rates = data['rates']
print(rates)
print(type(rates))
# [{'no': '019/A/NBP/2024', 'effectiveDate': '2024-01-26', 'mid': 4.0393}]
rate = rates[0]
print(type(rate))  # <class 'dict'>
print(rate['mid'])  # 4.0393
