import string

with open('story.txt', 'r') as ff:
    text = ff.read()

print(text)
text = text.strip()
#text = text.replace(",", "").replace(".", "").replace("!", "")
# print(string.punctuation)
for symbol in string.punctuation:
    text = text.replace(symbol, "")
print(text)

words = text.split()
print(words)

