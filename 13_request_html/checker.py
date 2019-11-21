import sys

args = sys.argv

if len(args) == 3:
    dict_file_name = args[1]
    text_file_name = args[2]
else:
    print("""Script usage is:
python.exe checker.py dict_file_name text_file_name

where: 
    dict_file_name -- dictionary file mane  
    text_file_name -- file name for spell analysis  
     """)
    sys.exit(1)

print(dict_file_name)
print(text_file_name)

text_dict = ""
with open(dict_file_name, "r") as file_dict:
    text_dict = file_dict.read()

text_for_check = ""
with open(text_file_name, 'r') as file_text:
    text_for_check = file_text.read()

print(len(text_dict))
print(len(text_for_check))
