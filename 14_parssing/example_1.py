import requests
import bs4

responce = requests.get("http://quotes.toscrape.com/")

# print(responce.text)

soup = bs4.BeautifulSoup(responce.text, 'html.parser')
print(soup.title.string)
divs = soup.find_all("div", {"class":"qoute"})
print(len(divs))

