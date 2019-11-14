x = 5
L = []


def foo(x, L=[]):
    L.append(x)
    print("*", L)


print(L)
foo(x)
print(L)
foo(x)
print(L)
foo(x)
print(L)
