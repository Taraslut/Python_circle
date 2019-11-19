import requests

r = requests.get("http://codewars.com")

print(r)
print(r.text)