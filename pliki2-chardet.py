import chardet

#  pip install chardet
print(chardet)

file_path = "test.log"

with open(file_path, "rb") as file:
    raw_data = file.read()

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'MacRoman', 'confidence': 0.6460919540229885, 'language': ''}
# po zwiekszeniu próbki
# {'encoding': 'utf-8', 'confidence': 0.87625, 'language': ''}
encoding = result['encoding']
print(encoding)  # utf-8
print(raw_data)
# b'Powitanie\r\nKolejne\r\nJeszcze jedno\r\nDodane\r\nDodane\r\nDodane\r\nDodane\r\nDodane\r\nDo\xc4\x85c\xc5\x84\xc5\x9bdane\r\n'
print(raw_data.decode(encoding=encoding))
# Powitanie
# Kolejne
# Jeszcze jedno
# Dodane
# Dodane
# Dodane
# Dodane
# Dodane
# Doącńśdane
