# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284

#Решение 1

k = int(input('k = '))
setrecursionlimit(10**5)


def pairs(array):
    if len(array) == 0:
        return
    pairless = array.pop(0)
    for i in array:
        if i[0] == pairless[1] and i[1] == pairless[0]:
            print(f'{pairless[0]} {i[0]}')
    return pairs(array)


def denominators(n, s=1, all_numbers_denominators=None):
    if all_numbers_denominators is None:
        all_numbers_denominators = []
        if s > n:
            return all_numbers_denominators
    denominator_sum = 0
    for i in range(1, s // 2 + 1):
        if s % i == 0:
            denominator_sum += i
            all_numbers_denominators.append((s, denominator_sum,))
    return denominators(k, s+1, all_numbers_denominators)


pairs(denominators(k))

#Решение 2

k = 10000 


def get_sum(n):
    current_sum = 1
    for element in range(2, n):
        if n % element == 0:
            current_sum += element
    return current_sum


def fill_arrays(k):
    res = list()
    for n in range(1, k+1):
        if n not in res:
            m = get_sum(n)
        if n == get_sum(m) and m != n:
            res.append(m)
            res.append(n)
    return res


print(fill_arrays(k))