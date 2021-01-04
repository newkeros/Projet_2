"""Main file to run"""

from parserbook import get_all_product_infos
from Get_category_books import get_category_books
from CSV_creator import create_csv
from Pictures import get_picture
from Categories_urls import collect_categories_urls
from tqdm import tqdm


if __name__ == "__main__":

    all_categories_urls = collect_categories_urls("https://books.toscrape.com/")
    for categories_urls in tqdm(all_categories_urls):

        category_url_list = get_category_books(categories_urls)

        for urls in category_url_list:
            category_dict = get_all_product_infos(urls)
            create_csv(category_dict)
            get_picture(category_dict)
