# funkcje - kawałek kodu, który możemy wykonac wielokrotnie
# funkcja musi byc najpierw zadeklarowana
# funkcja musi byc osobno uruchomiona

a = 6
b = 7


# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    """
    funkcja operująca na argumentach z globalnego scopa
    :return: None
    """
    print(a + b)


def dodaj2(a, b):  # funkcja posiada dwa argumenty obowiązkowo
    print(a + b)


# zasymulowana moliwosc przeciąania argumentów funkcji
def odejmij(a, b, c=0):  # funkcja z argumentem domyslnym
    print(a - b - c)


# wykonanie funkcji
# nazwa funkcji i nawiasy okrągłe
dodaj()  # 13
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
# argumenty przekzane pozycyjnie
dodaj2(5, 7)  # 12
odejmij(1, 2, 3)
odejmij(1, 2)  # c=0
# argumenty przekazane po nazwie
odejmij(b=9, a=8)
odejmij(1, b=8, c=9)
# odejmij(b=1, 8, c=9)  # SyntaxError: positional argument follows keyword argument
odejmij(c=9, b=9, a=5)
# print(dodaj2(7,9) + dodaj())  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
