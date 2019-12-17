import requests
import bs4  # beautifulsoup4

page = 1
url = ""
while True:
    print("="*10, page, "="*10)
    page += 1
    base_url = "http://quotes.toscrape.com"
    response = requests.get(base_url + url)

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    rez = soup.find_all("div", {'class': 'quote'})

    for item in rez:
        main_text = item.span.text
        print(main_text)
        author = item.find('small').text
        print(author)
        print("-" * 40)

    try:
        url = soup.find("li", {'class': "next"}).a['href']
    except Exception:
        break
