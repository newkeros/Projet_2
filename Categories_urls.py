"""Collect all categories urls"""

from bs4 import BeautifulSoup
import requests


def collect_categories_urls(website_url):
    response = requests.get(website_url)
    soup = BeautifulSoup(response.text, "lxml")
    links_list = list()
    for links in soup.findAll("a")[3:53]:
        links_list.append("http://books.toscrape.com/" + links.get("href"))
    return links_list
