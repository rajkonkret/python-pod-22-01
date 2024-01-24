import pandas

# pip install pandas

data = pandas.read_csv('records.csv', delimiter=";")

print(data)
#     name branch  year  cgpa
# 0  radek    coe     3   0.0
# 1  radek    coe     3   0.0
# 2  tomek    cos     2   0.1
# 3  zenek    cot     1   0.9
# 4  tadek    sdf     0   2.0

print(data.values)
# [['radek' 'coe' 3 0.0]
#  ['radek' 'coe' 3 0.0]
#  ['tomek' 'cos' 2 0.1]
#  ['zenek' 'cot' 1 0.9]
#  ['tadek' 'sdf' 0 2.0]]
print(data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(type(data))  # <class 'pandas.core.frame.DataFrame'>
print(type(data.values))  # <class 'numpy.ndarray'>
print(data.values[0])  # ['radek' 'coe' 3 0.0]
print(data.items)
# 0  radek    coe     3   0.0
# 1  radek    coe     3   0.0
# 2  tomek    cos     2   0.1
# 3  zenek    cot     1   0.9
# 4  tadek    sdf     0   2.0>
