# match case
# python 3.10

lista = []

lang = input("Podaj znany ci język programowaia")  # string

match lang.lower().replace(" ", ""):
    case "python":
        lista.append("Python")
    case "java":
        lista.append("Java")
    case "c++":
        lista.append("C++")
    case "1" | "2" | "3" | "4" | "5" | "6":
        lista.append(lang)
    case _:  # wartosc domyslna
        print("Nie znaleziono język programowania")

print(lista)
