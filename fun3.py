a = 10
b = 10


def dodaj():
    a = 6
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a
    a = 6  # uzywamy globanej zmiennej o nazwie a, zmieniamy wartość globalną
    b = 8
    print(a + b)


print('Zmienna a z góry:', a)  # Zmienna a z góry: 10
dodaj()  # funkcja ma LOKALNE zmienne a i b ale nie nadpisuje wartości globalnych
print('Zmienna a z góry:', a)  # Zmienna a z góry: 10 - zmienna globalna a nie zmieniła wartosci
dodaj2()  # 20 ROBI OBLICZENIA NA GLOBALNYM A I B
print('Zmienna a z góry:', a)  # Zmienna a z góry: 10
dodaj3()  # 14
print('Zmienna a z góry:', a)  # Zmienna a z góry: 6
