# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

list1 = [1, 3, 3, 3, 4]
min_score = min(list1)
max_score = max(list1)
list2 = []
for elem in list1:
    if elem == max_score:
        list2.append(min_score)
    else:
        list2.append(elem)

print(list2)

print([min_score if elem == max_score else elem for elem in list1])


def func(list1, list2=[], min_score=min(list1), max_score=max(list1)):
    if len(list1) == 0:
        return list2
    if list1[0] == max_score:
        list2.append(min_score)
    else:
        list2.append(list1[0])
    return func(list1[1:], list2)

print(func(list1))
