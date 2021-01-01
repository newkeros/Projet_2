# File to make the request

import requests
from bs4 import BeautifulSoup


def request(url):
    try:
        # request va récupérer les données html
        response = requests.get(url)
        if response.ok:
            response.encoding = "utf-8"
            # BS va récupérer le texte avec lxml pour parser les infos
            soup = BeautifulSoup(response.text, 'lxml')
            return soup
    except requests.ConnectionError:
        print("Connexion Error")

