# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

count = 1
k = 2
res = 1
while res <= n:
    print(res)
    res = k ** count
    count += 1

# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1            ИДЕАЛЬНОЕ РЕШЕНИЕ