def foo(num, target= None):
    if target is None:
        target = []
    target.append(num)
    return target

l = []
print(foo(1, l))
print(foo(2, l))
print(foo(3))