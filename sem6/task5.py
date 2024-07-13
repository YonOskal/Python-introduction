def func1(n):
    res = [el for el in range(n)]
    return res

print(func1(5))

def func2(n):
    for el in range(n):
        yield el

for el in func2(5):
    print(el, end = " ")

print({el: el for el in range(5)})