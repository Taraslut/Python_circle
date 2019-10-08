# s = 'Привіт це я \'звертаюся\' до вас.'
# s = input("Enter some words>> ")
s = "Hello world!"
print(s)
print(len(s)) # len - lenght
print(s[0])

for i in range(len(s)):
    print(s[i], end="")
print()

print(s[0:4])

s = s.lower()
print(s.lower())
print(s.replace("world", "Taras"))
print(s)

