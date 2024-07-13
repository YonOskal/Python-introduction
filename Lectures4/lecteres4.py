def f(x):
    return x*x
print(f(6))

def math(op, x, y):
    print(op(x,y))

math(lambda a,b: a + b, 5, 45)

my_list = [1, 2, 3, 5, 8, 15, 23, 38]
res = {}

for elem in my_list:
    if elem % 2 == 0:
        res[elem] = elem**2
print(res)

def select(f, col):
    return [f(x) for x in col]

def where(f,col):
    return [x for x in col if f(x)]

res = select(int, my_list)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)

num = [1, 2, 3, 4]
add = map(lambda a: a + a, num)
print(add)

points = [(1, 2), (3, 1), (5, 0)]
sorted_points = sorted(points, key=lambda x: x[0])
print(sorted_points) 