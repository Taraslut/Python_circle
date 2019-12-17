import re
import requests
import bs4

url = ""
start_url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

while True:
    url = start_url + url
    responce = requests.get(url)

    # print(response.text)

    soup = bs4.BeautifulSoup(responce.text, 'html.parser')
    rez = soup.find('p', {'class': re.compile("star.*")})
    print(rez['class'][1])

    rezz = soup.find_all("th")
    upc = ''
    for item in rezz:
        if item.text == "UPC":
            upc = item.next_sibling.text

    print(upc)
    break
    # print(soup.title.string)
    divs = soup.find_all("div", {"class":"quote"})
    print(len(divs))
    try:
        next_link = soup.find('li', {'class':'next'})
        # print(next_link)
        url = next_link.a['href']
        print("-"*20, str(url).split("/")[-2], "-"*20)
    except:
        break



