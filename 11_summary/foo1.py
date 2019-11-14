foo = ['foo']
bar = foo

print(id(foo), id(bar))
print(foo)
bar += ['bar']
print(foo, bar)
print(id(foo), id(bar))
print("*" * 20)

x = 5
y = x
print(id(x), id(y))
y += 4
print(x, y)
print(id(x), id(y))
print("*" * 20)

x = (5, 6)
y = x
print(id(x), id(y))
y += (7,)
print(x, y)
print(id(x), id(y))
print("*" * 20)

dd = {'a': 1, 1: 'a'}
ll = dd
print(id(dd), id(ll))
ll.update({2: 3})
print(dd, ll)
print(id(dd), id(ll))
