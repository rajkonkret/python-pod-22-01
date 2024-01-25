# dekorator - funkcja przyjmująca funkcje jako argument i dodająca do niej nową funkcjonalność

def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()  # zwracamy wynik funkcji, ktora została do nas przekazana

    return wew  # zwroc wynik


def upper_case_decorator(f):
    def wrapper():
        result = f()
        return result.upper()

    return wrapper


@dekor
def hej():
    print("Hej")


@upper_case_decorator
def greeting():
    return "Hallo World!!!"


hej()
# bez dekoratora -> Hej
# Dekorujemy
# Hej
print(greeting())  # HALLO WORLD!!!
