weekdays = []
print(weekdays)
weekdays = ['Monday', "Tuesday", 'Weednesday']
print(weekdays)
# first item in the list
print(weekdays[0])
#slice
print(weekdays[0:2])

another_list = list()
print(another_list)

# iterate by string
ll1 = list('cat')
print(ll1)

ll2 = ['cat']
print(ll2)

ll3 = ['cat', 'dog']
print(ll3)

# # error
# ll4 = list('cat', 'dog')
# print(ll4)

# magic :)
ll4 = list(('cat', 'dog'))
print(ll4)