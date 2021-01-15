import requests
from bs4 import BeautifulSoup


def request(url):
    """Make the request on the website"""
    try:
        response = requests.get(url)
        if response.ok:
            response.encoding = "utf-8"
            soup = BeautifulSoup(response.text, "lxml")
            return soup
    except requests.ConnectionError:
        print("Connexion Error")
