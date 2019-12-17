import requests
import bs4

template = "https://ukr.net"
page = requests.get(template)



# print(page.text)

bs_page = bs4.BeautifulSoup(page.text, "html.parser")
print('='*40)
print(bs_page.get_text())