def foo(num, target=[]):
    target.append(num)
    print(id(target))
    return target


print(foo(1))
print(foo(2))
print(foo(3))
