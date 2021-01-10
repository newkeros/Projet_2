# Utilisez les bases de Python pour l'analyse de marché



[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)




## What’s the purpose of this script

This script let you parse and scrape informations from [books.toscrape.com](https://books.toscrape.com/index.html) website. When you run it, it scrapes the website and export to CSV files all books informations from each category. It also download all books images for each category.




## What do you need to run this project

In the requirements.txt you will find all the following libraries. These libraries are mandatory to run the script.

* beautifulsoup4==4.9.3
* certifi==2020.6.20
* chardet==3.0.4
* idna==2.10
* lxml==4.5.2
* requests==2.24.0
* soupsieve==2.0.1
* urllib3==1.25.10
* tqdm==4.55.0


## Set up the project

This project is made with Python 3

Clone it on your computer with the git clone command : `<Git clone https://github.com/newkeros/Projet_2.git>`

Create a virtual environment with `<cd Projet_2 -m venv env>` and activate it

Install the libraries with `<install -r requirements.txt>`


## Run the project

Execute the main.py file with the folder path you want the script to go in `<python main.py <path_you_decide>`

A data folder will be created. In this folder, the script will create a folder for each category. In each category folder, a CSV file with books informations will be created. A folder with all the images from this category will be created as well.

**Disclaimer** : Please be patient, the script needs approximatively 13 minutes to be fully run.


## Made with

* OpenClassrooms website
* Requests, Urllib3 and BeautifulSoup4 documentations
* Python crash course book from Eric Matthes
* The continuous help of my mentor





