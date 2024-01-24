import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter, dialect.quotechar, dialect.escapechar)  # ; " None
    csv_f.seek(0)  # powrót wskanika na początek pliku
    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)
    print(csvreader)  # <_csv.reader object at 0x000002149B341900>

    fields = next(csvreader)  # pobranie pierwszego wiersza z pliku csv, ustawienie wskaźnika na następny
    for row in csvreader:  # wystartuje od wiersza drugiego czyli od indeksu 1 1...konca pliku
        rows.append(row)

print(fields)
print(rows)
# ['name;branch;year;cgpa']
# [['radek;coe;3;0'], ['radek;coe;3;0'], ['tomek;cos;2;0.1'], ['zenek;cot;1;0.9'], ['tadek;sdf;0;2']]
# po ustawieniu delimiter=";"
# ['name', 'branch', 'year', 'cgpa']
# [['radek', 'coe', '3', '0'], ['radek', 'coe', '3', '0'], ['tomek', 'cos', '2', '0.1'], ['zenek', 'cot', '1', '0.9'],
#  ['tadek', 'sdf', '0', '2']]
# ; " None
# < _csv.reader
# object
# at
# 0x000001F11A791900 >
# ['name', 'branch', 'year', 'cgpa']
# [['radek', 'coe', '3', '0'], ['radek', 'coe', '3', '0'], ['tomek', 'cos', '2', '0.1'], ['zenek', 'cot', '1', '0.9'],
#  ['tadek', 'sdf', '0', '2']]
