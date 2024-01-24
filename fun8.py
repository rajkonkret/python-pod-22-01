def allparams(a, b, /, c=42, *args, d=90, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print('args', args)
    print('kwargs', kwargs)


allparams(1, 2)  # a, b 1 2
allparams(1, 2, c=100)  # c, d 100 90
allparams(1, 2, 3)
# allparams(a=1, b=2)  # TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# / - oddziela argumenty mozliwe do przekazanie po pozycji od tych po nazwie lub po pozycji
# a i b tylko po pozycji
allparams(1, 2, a=2, b=4)  # kwargs {'a': 2, 'b': 4}
# allparams(1, 2, c=9, 4)  # SyntaxError: positional argument follows keyword argument
# gdy chcemy podac argumenty do argsów, to musimy c podac po pozycji bo nie można podawac argumentów pozycyjnych po nazwanych
allparams(1, 2, 9, 4, 5, 6, 7, 8, 9, 0, 10, 45, 67, 8, 9, 89, 99)
# args (4, 5, 6, 7, 8, 9, 0, 10, 45, 67, 8, 9, 89, 99)
# d - tak naprawdę możemy przekazać tylko po nazwie bo nie da sie zakończyc argsów w inny sposób
allparams(1, 2, 9, 4, 5, 6, 7, 8, 9, 0, 10, 45, 67, 8, 9, 89, 99, d=100)  # c, d 9 100
# kolejne argumenty klucz wartosc (nazwane) trafia do słownika
allparams(1, 2, 9, 4, 5, 6, 7, 8, 9, 0, 10, 45, 67, 8, 9, 89, 99, d=100, x=100)  # c, d 9 100
allparams(1, 2, 9, 4, 5, 6, 7, 8, 9, 0, 10, 45, 67, 8, 9, 89, 99, d=100, x=100, a=9, b=78)
# kwargs {'x': 100, 'a': 9, 'b': 78}
