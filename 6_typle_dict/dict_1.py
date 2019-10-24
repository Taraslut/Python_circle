dd = {}
print(dd, "==>", type(dd))
dd['ivan'] = "Galyts'ka str. 12"
dd[2] = "Nezaledjnosti str. 1"
print(dd)

for key in dd:
    print(key, "====> ", dd[key])
print('*'*20)
del dd[2]
print(dd)

dd[1] = ()
print(dd)
print(len(dd))
print(dd.keys())
print(dd.values())

# error
dd[ (2,1) ] = "sdfsd"
print(dd)