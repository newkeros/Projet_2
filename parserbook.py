"""Parse all data needed and put it in a dictionary"""

from request import request


def get_title(article):
    """Return the title of a book"""
    title = article.find("div", class_="col-sm-6 product_main").h1.text
    return title


def get_product_upc(article):
    """Return the product UPC from a book"""
    tableau = article.select("tr")
    return tableau[0].td.text


def get_product_description(article):
    """Return the product description of a book"""
    product_description_text = article.select("p")
    return product_description_text[3].text


def get_price_including_tax(article):
    """Return the price of a book including tax"""
    price_with_tax = article.select("tr")
    return price_with_tax[3].td.text


def get_price_excluding_tax(article):
    """Return the price of a book excluding tax"""
    price_without_tax = article.select("tr")
    return price_without_tax[2].td.text


def get_number_available(article):
    """Return the number of books available"""
    number_available = article.select("p")
    return number_available[1].text.strip().strip(" Instock)available(")


def get_category(soup):
    """Return the name of the category"""
    category = soup.ul.find_all("a")[-1].text
    return category


def get_review_rating(article):
    """Return the book review rating"""
    review_rating = article.find_all("p")[2]
    return review_rating.get("class")[-1]


def get_image_url(article):
    """Return the image url"""
    get_image = article.find_all("img")[0]
    return get_image.get("src").replace("../../", "http://books.toscrape.com/")


def get_all_product_infos(url):
    """Return a dictionnary will all book informations"""
    product_infos = dict()
    soup = request(url)
    article = soup.find("article")
    product_infos["product_page_url"] = url
    product_infos["product_upc"] = get_product_upc(article)
    product_infos["title"] = get_title(article)
    product_infos["price_including_tax"] = get_price_including_tax(article)
    product_infos["price_excluding_tax"] = get_price_excluding_tax(article)
    product_infos["number_available"] = get_number_available(article)
    product_infos["product_description"] = get_product_description(article)
    product_infos["category"] = get_category(soup)
    product_infos["review_rating"] = get_review_rating(article)
    product_infos["image_url"] = get_image_url(article)
    return product_infos
