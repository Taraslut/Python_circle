import requests
import bs4 as bs


r = requests.get("http://quotes.toscrape.com")

print(r)
print(r.text)
print("="*40)

soup = bs.BeautifulSoup(r.text, "html.parser")

print(soup.text)

for n, i in enumerate(soup.find_all("div", {"class": "quote"})):
    print("-"*20, n,"-"*20, )
    print(i.text)

