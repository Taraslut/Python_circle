ll = [2, 25]
print(ll)

ll.append(45)
print(ll)

ll.extend([32, 67, 89])
# ll.append([32, 67, 89])
print(ll)

position = ll.index(32)
print(32, " placed in ", position, "-th position", sep="")
print(f"{32} placed in {position}-th position")

ll.remove(25)
# ll.remove(5) << error WHY?
print(ll)

ll.pop(0)
# print(item)
print(ll)
print(f"The length of the list is {len(ll)} items.")
# ll.sort()
# print(ll)

ll.reverse()
print(ll)



