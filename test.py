a = 1
b = 5
division = []
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            division.append(j)
    if len(division) == 2:
        print(i)
    division.clear()