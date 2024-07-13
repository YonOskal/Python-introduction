# Задача №3.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def func1(n):
    for i in range(2, n):
        if n % i == 0:
            return "no"
    return "yes"
print(func1(5))

def func2(n, i=2):
    if i < n:
        if n % i == 0:
            return "no"
        return func2(n, i+1)
    return "yes"
print(func2(5))



