class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    # print(5 / 0)
    raise ZeroDivisionError("Nie dziel przez zero")
except ZeroDivisionError:
    print("Nie dziel przez zero")

x = 0
try:
    if x == 0:
        raise MyException("X nie może byc 0")
except MyException:
    print("X nie moze byc zero")
