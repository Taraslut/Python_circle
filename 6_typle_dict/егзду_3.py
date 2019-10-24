tt = (2, 5, 8)
for num, i in enumerate(tt):
    print(num, "-th  ->", i)
# !!!!!!!
mm = min(tt)
maxx = max(tt)
ss = sum(tt)
print(mm, maxx, ss)

tt1 = ("cake", "cookies", 'apple')
tt2 = (25, 1.2, 12)
tt3 = ['I-F', "Lviv", "Kyiv"]

for first, second, last in zip(tt1, tt2, tt3):
    print(f'{first} ==> {second}$ in {last} city.')

print(type(tt1))
tt1 = list(tt1)
print(type(tt1))
tt1[0] = 12
tt1 = tuple(tt1)
print(tt1, type(tt1))
