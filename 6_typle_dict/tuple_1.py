tt = 12, "hello", 32
print(tt)
print(type(tt))
print(id(tt))

var = tt[0]
print(var)
x, y, z = tt
print(x)
print(z)
print(y)

tt = x, y, z + 1000
# tt[0] = 25
tt = (25,) +  tt[1:]
print(tt)
print(id(tt))

ll= []
print(ll, id(ll))
ll.append(1)
print(ll, id(ll))

for i in tt:
    print(i)
