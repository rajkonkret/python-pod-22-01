import shutil
from pathlib import Path

base_path = Path('ops_example')
base_path2 = Path('ops_example/D')

print(base_path)
print(base_path2)
# ops_example
# ops_example\D

if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)

base_path.mkdir()

path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

# path_b.mkdir()  # FileNotFoundError: [WinError 3] System nie może odnaleźć określonej ścieżki: 'ops_example\\A\\B'
path_b.mkdir(parents=True)
path_c.mkdir()
for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, 'w', encoding='utf-8') as stream:
        stream.write(f"Jakaś treść pliku {filename}")

# przeniesienie katalogu
shutil.move(path_b, path_d)
ex1 = path_d / 'ex1.txt'
ex1.rename(ex1.parent / 'ex1renamed.log')  # zmiana nazwy pliku

print(base_path.absolute())
print(base_path2.absolute())
# C:\Users\CSComarch\PycharmProjects\python-pod-22-01\ops_example
# C:\Users\CSComarch\PycharmProjects\python-pod-22-01\ops_example\D
