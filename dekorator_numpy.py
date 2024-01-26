import time
import numpy as np


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_function():
    pass


@measure_time
def my_wait():
    time.sleep(2)  # wstrzymuje dany wątek na 2s


@measure_time
def my_for_sum():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print('Sum is:', suma)


@measure_time
def my_sum_without_for():
    total = sum(range(15_000_000))
    print("sum is:", total)


@measure_time
def my_sum_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print('Sum is:', total)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 200, 300, 400, 500, 600, 700, 800, 900]
lista2 = list(range(1_000_000))


@measure_time
def my_for_without_map():
    l = []
    for x in range(1):
        for i in lista2:
            l.append(i * 2)
    # print("Lista:", l)


@measure_time
def my_for_with_map():
    l_map = []
    for x in range(1):
        l_map = list(map(lambda x: x * 2, lista2))
    # print("Lista:", l_map)


print("----sum----")
my_function()  # Czas wykonania funkcji my_function: 0.0
my_wait()  # Czas wykonania funkcji my_wait: 2.0011892318725586
my_for_sum()  # Czas wykonania funkcji my_for_sum: 0.8418281078338623
my_sum_without_for()  # 0.5754554271697998
my_sum_np()  # 0.0329127311706543

print("----map----")
my_for_with_map()  # Czas wykonania funkcji my_for_with_map: 0.10568833351135254
my_for_without_map()  # # Czas wykonania funkcji my_for_without_map: 0.07778620719909668
# Czas wykonania funkcji my_function: 0.0
# Czas wykonania funkcji my_wait: 2.000666856765747
# Sum is: 112499992500000
# Czas wykonania funkcji my_for_sum: 0.9016318321228027
# sum is: 112499992500000
# Czas wykonania funkcji my_sum_without_for: 0.578873872756958
# Sum is: 112499992500000
# Czas wykonania funkcji my_sum_np: 0.030024290084838867
# ----------
# Czas wykonania funkcji my_for_with_map: 0.10568833351135254
# Czas wykonania funkcji my_for_without_map: 0.07778620719909668
