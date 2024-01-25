import pickle

lista = [1, 2, 3, 4, 5]

with open('test_lista.txt', 'w') as f:
    f.write(str(lista))

with open('test_lista.txt', "r") as f:
    dane = f.read()

print(dane)
print(type(dane))  # <class 'str'>
print(list(dane))  # ['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ',', ' ', '5', ']']
print(dane[0])  # [

with open('test_pickle.pickle', 'wb') as f:
    pickle.dump(lista, f)

with open('test_pickle.pickle', 'rb') as f:
    loaded_list = pickle.load(f)

print(loaded_list)  # [1, 2, 3, 4, 5]
print(type(loaded_list))  # <class 'list'>
print(loaded_list[0])  # 1

# serializacja listy
ser_lista = pickle.dumps(lista)
print(ser_lista)  # b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'
# deserializacja
print(pickle.loads(ser_lista))  # [1, 2, 3, 4, 5]
