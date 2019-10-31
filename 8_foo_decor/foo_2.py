def sub(a, b):
    rez = a - b
    return rez

def add(x, y):
    return x + y

def func(ff, a, b):
    rez = ff(a, b)
    return rez

print(func(add, 2, 3))

# func(print, 2, 3)

print(func(add, [1,2], [3,4]))

# print([1,2] + [3,4])

print(func(add, "Hello ", "world!"))

print(func(add, "Hello ", 2))