def connect(**opcje):  # ** argumenty słownikowe
    print(opcje)
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    connect_param['pwd'] = opcje
    print(connect_param)


def all_args(*args, **kwargs):
    print(args)
    print(kwargs)


connect()
connect(a=9)
connect(a=9, b=9, name="Radek")  # {'a': 9, 'b': 9, 'name': 'Radek'}
print("radek", "tomek", 1, 2, 3)  # radek tomek 1 2 3
all_args()
all_args(1, 2, 3)
all_args(1, 2, a=9, b=90)
