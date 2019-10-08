s = "asdasd"
s.title()
print(s[1:4])
print(s[1:])
print(s[:])
print(s[:4])
print(s[:-1])
s = s.title()
id(s)
# s[0] ='a' << ERROR
s = "a" + s[1:]
print(s)
print(s [1::2])
print(s [::-1])
print(s)
s= "hello gter dfgdfg dfwert 456"
s_spl = s.split()
s_spl
s_spl[0]
s_spl[1]
for i in range(len(s_spl)):
    print(i)

# print word by word
for i in range(len(s_spl)):
    print(s_spl[i])
ss = "      hello world         "
print(ss)
print(ss.strip())
'''
введи кільк годин >> 4.6
в 4.6 год це є 276 хв
'''

''''
petrov      petro  Ivanovychhhhhhhh Ssemenovyyych
PPIS
'''
'''
Palindrom Task?
asdfgfdsa -- True
asddsa  -- True
asdfgdsa  -- False
'''
