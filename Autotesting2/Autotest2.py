# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

list_1 = [1, 11, 14, 7, 8, 15]
k = 11
min_variance = 100
for i in range(len(list_1)):
    if k > list_1[i]:
        variance = k - list_1[i]
        if  variance < min_variance:
            min_variance = variance
            res = list_1[i]
    elif k < list_1[i]:
        variance = list_1[i] - k
        if  variance < min_variance:
            min_variance = variance
            res = list_1[i]
    else:
            res = list_1[i]
            break

print(res)

        
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

#          ИДЕАЛЬНОЕ РЕШЕНИЕ
