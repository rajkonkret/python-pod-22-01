# csv - pliki gdzie dane przedzielone znakiem podziału (,; spacja tab)
# Zenek, Marek, Tomek

import csv

# csv - biblioteka do pracy z plikami csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '0']

filename = 'records.csv'

dict = dict(zip(fields, row))
print(dict)  # {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0'}

dict_list = [
    {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0'},
    {'name': 'tomek', 'branch': 'cos', 'year': '2', 'cgpa': '0.1'},
    {'name': 'zenek', 'branch': 'cot', 'year': '1', 'cgpa': '0.9'},
    {'name': 'tadek', 'branch': 'sdf', 'year': '0', 'cgpa': '2'},
]
with open(filename, 'w', newline='') as csv_f:
    # proste uzycie, zapis wiersz po wierszu
    # csvwriter = csv.writer(csv_f)
    # csvwriter.writerow(fields)
    # csvwriter.writerow(row)
    # zapisywanie csv z danych słownikowych
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerow(dict)
    # zapisanie danych z listy słowników
    csvwriter.writerows(dict_list)
# newline='' - ni edopisuje pustych linii między wierszami
# delimiter=";" - ustawia znak oddzielajacy na średnik ;
