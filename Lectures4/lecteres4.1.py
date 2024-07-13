# list_1 = [x for x in range(1,20)]

# print(list_1)

data = "12 12 346 763 34 63"
data2 = "45 63 756 12"

print(data)
data = list(map(int, data.split()))
print(data)

data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)


