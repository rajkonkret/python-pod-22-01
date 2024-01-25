# wielodziedziczenie
class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(B, A):  # kolejnosc ma znaczenie
    """
    Dziedziczy po B i A
    """


class D(A, B):
    def method(self):
        super().method()


class E(B, A):
    def method(self):
        print("Metoda z klasy E")


class F(A, B):
    def method(self):
        B.method(self)


class G(A, B):
    def method(self):
        super().method()
        B.method(self)
        print("Metoda z klasy G")


a = A()
a.method()

b = B()
b.method()
# Metoda z klasy A
# Metoda z klasy B
c = C()
c.method()
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
d = D()
d.method()

e = E()
e.method()  # Metoda z klasy E

f = F()
f.method()  # Metoda z klasy B

g = G()
g.method()
# Metoda z klasy A
# Metoda z klasy B
# Metoda z klasy G
# __mro__ - kolejnoasc roziazywania nazw
print(G.__mro__)
# (<class '__main__.G'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
