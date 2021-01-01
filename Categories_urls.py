from bs4 import BeautifulSoup
import requests


def collect_categories_urls(website_url):
    response = requests.get(website_url)
    soup = BeautifulSoup(response.text, 'lxml')
    mylist = list()
    for links in soup.findAll('a')[3:53]:
        mylist.append("http://books.toscrape.com/" + links.get('href'))
    return mylist



