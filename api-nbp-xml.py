import requests
import xml.etree.ElementTree as ET

url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'
response = requests.get(url)
print(response)  # <Response [200]>

xml_data = response.content
print(xml_data)

root = ET.fromstring(xml_data)
print(root)  # <Element 'ArrayOfExchangeRatesTable' at 0x0000021CF63678D0>

table_name = root.find(".//Table").text
print(f'Table: {table_name}')  # Table: A

date = root.find(".//EffectiveDate").text
print(f"Date: {date}")  # Date: 2024-01-26

no = root.find(".//No").text
print(f'Numer tabeli: {no}')  # Numer tabeli: 019/A/NBP/2024

rates = root.findall('.//Rate')
print(rates)

# < Rate >
# < Currency > bat(Tajlandia) < / Currency >
# < Code > THB < / Code >
# < Mid > 0.1134 < / Mid >
# < / Rate >
for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = rate.find('Mid').text
    print(f"{code}: {currency} - {mid}")
# THB: bat (Tajlandia) - 0.1134
# USD: dolar amerykański - 4.0393
# AUD: dolar australijski - 2.6622
# HKD: dolar Hongkongu - 0.5168
# CAD: dolar kanadyjski - 3.0019
# NZD: dolar nowozelandzki - 2.4649
# SGD: dolar singapurski - 3.0131
# EUR: euro - 4.3802
# HUF: forint (Węgry) - 0.011343
# CHF: frank szwajcarski - 4.6690
# GBP: funt szterling - 5.1357
# UAH: hrywna (Ukraina) - 0.1069
# JPY: jen (Japonia) - 0.027322
# CZK: korona czeska - 0.1769
# DKK: korona duńska - 0.5875
# ISK: korona islandzka - 0.029576
# NOK: korona norweska - 0.3865
# SEK: korona szwedzka - 0.3869
# RON: lej rumuński - 0.8802
# BGN: lew (Bułgaria) - 2.2395
# TRY: lira turecka - 0.1332
# ILS: nowy izraelski szekel - 1.0885
# CLP: peso chilijskie - 0.004438
# PHP: peso filipińskie - 0.0717
# MXN: peso meksykańskie - 0.2355
# ZAR: rand (Republika Południowej Afryki) - 0.2148
# BRL: real (Brazylia) - 0.8215
# MYR: ringgit (Malezja) - 0.8544
# IDR: rupia indonezyjska - 0.00025533
# INR: rupia indyjska - 0.048581
# KRW: won południowokoreański - 0.003026
# CNY: yuan renminbi (Chiny) - 0.5629
# XDR: SDR (MFW) - 5.3593
