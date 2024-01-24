# funkcja zagnieżdzona
# funkcja wewnętrzna
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwraca adres funkcji, referencje


xfun = fun1()
print(xfun)  # <function fun1.<locals>.fun2 at 0x0000014410FD8AE0>
print(type(xfun))  # <class 'function'>
xfun()  # To jest fun2
