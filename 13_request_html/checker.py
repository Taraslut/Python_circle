import sys

args = sys.argv

print(args)

if len(args) == 3:
    dict_file_name = args[1]
    text_file_name = args[2]
else:
    print("Ви погані")

print(dict_file_name)
print(text_file_name)
