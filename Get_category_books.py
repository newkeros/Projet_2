# File to get all books url from a category

from bs4 import BeautifulSoup
import requests


def get_category_books(category_url):
    base_url = category_url[:-10]
    next_flag = True
    books_urls = list()
    i = 1
    while next_flag:
        response = requests.get(category_url)
        soup = BeautifulSoup(response.text, 'lxml')
        for link in soup.find_all('h3'):
            books_urls.append(link.a.attrs['href'].replace('../../../', 'http://books.toscrape.com/catalogue/'))
        next_flag = soup.find("li", {"class": "next"}) is not None
        i += 1
        category_url = base_url + "page-" + str(i) + ".html"
    return books_urls











        #mettre dans une liste et chercher dans les differentes pages
        #liste de livre et dico de catégorie
   #récupérer url d'une page puis boucle pour plusieurs pages
   #va chercher tant qu'il y a un next parse les livres
   #titrer le csv avec le nom de la catégorie
   #refaire cours sur les fonction avec le passage en argument (input)
    #Puis on met toutes les url dans un dico
    #On parse les infos de chaque url de la liste
    #On envoie ces infos vers un nouveau csv

