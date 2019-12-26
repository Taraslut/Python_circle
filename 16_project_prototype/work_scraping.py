import bs4
import requests

start_url = "http://books.toscrape.com/"

with open("data.csv", "w") as f:
    main_page = requests.get(start_url)
    main_page_bs = bs4.BeautifulSoup(main_page.text, "html.parser")
    articles = main_page_bs.find_all('article', {"class":"product_pod"})

    urls = []
    for article in articles:
        urls.append(start_url + article.h3.a['href'])

    for url in urls:
        line = ""
        book_page = requests.get(url)
        book_page_bs4 = bs4.BeautifulSoup(book_page.text, "html.parser")
        title = book_page_bs4.h1.text
        line += "\"" + title + "\","
        price = book_page_bs4.p.text[2:]
        line += "\"" + price + "\","
        quant = book_page_bs4.find('p', {'class':'instock availability'}).text.strip()
        if len(quant) > 8:
            quant = int(quant.replace("In stock (", "").replace(" available)", ""))
        else:
            quant = 0
        line += "\"" + str(quant) + "\","

        f.write(line + "\n")
        # description --> str
        # UPS --> str
        # rating -- > int
        break
