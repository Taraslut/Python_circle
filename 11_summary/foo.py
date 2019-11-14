x = 5
y = 15

def my_foo(x, y):
    x,y = y, x

print(x,y)
my_foo(x, y)
print(x,y)

x = [5]
y = [10]

print(x,y)
my_foo(x, y)
print(x,y)



