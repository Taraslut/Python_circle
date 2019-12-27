import os

import bs4
import requests

mapping = {
    "One": '1',
    "Two": '2',
    "Three": '3',
    "Four": '4',
    "Five": '5'
}

start_url = "http://books.toscrape.com/"
next_page = ""

with open("data.csv", "w") as f:
    # heder row in csv-file
    # f.write()
    while True:
        main_page = requests.get(start_url + next_page)
        main_page_bs = bs4.BeautifulSoup(main_page.text, "html.parser")
        articles = main_page_bs.find_all('article', {"class": "product_pod"})

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
            quantity = book_page_bs4.find('p', {'class': 'instock availability'}).text.strip()
            if len(quantity) > 8:
                quantity = int(quantity.replace("In stock (", "").replace(" available)", ""))
            else:
                quantity = 0
            line += "\"" + str(quantity) + "\","

            description = book_page_bs4.find_all('p')[3].text
            line += "\"" + description + "\","

            UPS = book_page_bs4.find("th").next_sibling.text
            line += "\"" + UPS + "\","

            rating = book_page_bs4.find_all('p')[2]['class'][1]
            line += "\"" + mapping.get(rating, "0") + "\","

            var = book_page_bs4.find('div', {"class": "item"})
            img_url = start_url + var.img['src']
            img_data = requests.get(img_url, stream=True)
            base_dir = os.path.dirname(__file__)
            file_name = os.path.join(base_dir, "img", title.replace(" ", "_") + ".jpg")
            with open(file_name, "bw") as f_image:
                f_image.write(img_data.content)

            line += "\"" + file_name + "\","

            f.write(line.encode("utf-8").decode("ascii", "ignore") + "\n")

        next_page = main_page_bs.find("li", {'class': 'next'})
        if next_page is not None:
            next_page = start_url + next_page.a['href']
        else:
            break
