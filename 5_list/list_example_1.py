bord = [1 ,3, 5, -10]

print(bord)
# 1 -- add to the list 3, 5 , -10 ==>> 1, 3, 5, -10

# 2 find length of the list

# 3 find position of "3"

# 4 print neighbours of "5"

# 4' swap 5 <-> -10

# 5 print list by two elements in the line

print(bord)

index_1 = bord.index(5)
index_2 = bord.index(-10)
print(index_1, index_2)
temp = bord[index_1]
bord[index_1] = bord[index_2]
bord[index_2] = temp
print(bord)
# magic
bord[index_1], bord[index_2] = bord[index_2], bord[index_1]
print(bord)

# ll = [i for i in range(10)]
ll = []
for i in range(10):
    ll.append(i)
print(ll)