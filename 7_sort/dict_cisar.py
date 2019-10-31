import string

key = int(input('Enter key>>'))

str_arr = string.ascii_lowercase
str_arr2 = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
print(str_arr)
print(str_arr2)

cliper_dict= {}
for k, v in zip(str_arr, str_arr2):
    cliper_dict[k] = v
print(cliper_dict)
phrase = input(">>")
ss = ""
for letter in phrase:
    ss += cliper_dict[letter]
print(">", ss)