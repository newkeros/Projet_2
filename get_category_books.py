from bs4 import BeautifulSoup
import requests


def get_category_books(category_url):
    """Get all books urls from a category"""
    base_url = category_url[:-10]
    next_flag = True
    books_urls = list()
    i = 1
    while next_flag:
        response = requests.get(category_url)
        soup = BeautifulSoup(response.text, "lxml")
        for link in soup.find_all("h3"):
            books_urls.append(
                link.a.attrs["href"].replace(
                    "../../../", "http://books.toscrape.com/catalogue/"
                )
            )
        next_flag = soup.find("li", {"class": "next"}) is not None
        i += 1
        category_url = base_url + "page-" + str(i) + ".html"
    return books_urls
