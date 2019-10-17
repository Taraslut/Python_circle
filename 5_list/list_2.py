ll = ['spam', 'eggs', 100, 12.5]

for item in ll:
    print(item, type(item))
print()

for n, item in enumerate(ll):
    print(n, item, type(item))

# todo -- edit follow loop to print only ==>> 2 [100, 12.5]
for n, item in enumerate(ll):
    print(n , ll[n])


ll2 = ll + ["hello"]
print(ll2)
ll3 = ll2 * 3
print(ll3)

