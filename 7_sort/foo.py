def my_func(x, y, z=0):
    if z == 0:
        print("I got x=", x ,"and y=", y)
    else:
        print("I got x=", x, "and y=", y, ", z=", z)

my_func(x=5, y=10)
my_func(5, 10)
my_func(y=5, x=10)

# add third parameter 
my_func(5, 10 , 15)