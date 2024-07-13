# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

my_list = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"},
{"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {" VIII":"S007"}]

# традиционный итератор с методом add()
unique_values = set()
for item in my_list:
    for value in item.values():
        unique_values.add(value)
print(unique_values)

# set comprehension
print(set(value for item in my_list for value in item.values()))