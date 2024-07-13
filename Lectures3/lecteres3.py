# Возможность передачи неограниченного количества аргументов
# ● Можно указать любое количество значений аргумента функции.
# ● Перед аргументом надо поставить *.
# В примере ниже функция работает со строкой, поэтому при введении чисел
# программа выдаёт ошибку:

def concatenatio(*args):
    res = ""
    for item in args:
        res += item
    return res
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1')) # a1
print(concatenatio('7', '8', "6"))
# print(concatenatio(1, 2, 3, 4)) #