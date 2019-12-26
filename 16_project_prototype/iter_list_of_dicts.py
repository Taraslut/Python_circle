
list_of_dicts = [
    {'name':"one", "other":1},
    {'name':"two", "other":2},
    {'name':"one", "other":3},
]

rez = {}
my_name = "two"
for item in list_of_dicts:
    if my_name == item['name']:
       rez = item

print(rez)