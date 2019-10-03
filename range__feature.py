height = int(input("Enter height> "))
for i in range(height):
    for z in range(height - i):
        print(" ", end="")
    for k in range(i):
        print("#", end="")
    print()

