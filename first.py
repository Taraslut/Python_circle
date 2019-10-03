# max_i = int(input("Number>> "))

for i in range(8):
    if i % 2 == 0:# парне
        for item in range(4):
            print("**  ", end="")
    else:
        for item in range(4):
            print("  **", end="")

    print()
