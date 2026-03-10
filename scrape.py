# python -m pip install requests
# => get data from web (html, json, xml)
# python -m pip install beautifulsoup4
# => parse html

# install git
# go to terminal
# git config --global user.name "Ramesh Pradhan"
# git config --global user.email "pyrameshpradhan@gmail.com"

# git init
# git status=> if you want to check what are the status of files
# git add .  #track all files in current directory
# git commit -m "Your messages" #what u did
#create repository in github
#copy paste git code from github

# git => version control system

#########################
#1. change the code
#2. git add.
#3. git commit -m "Your message"
#4. git push
###############

import csv
import json
import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "http://books.toscrape.com/"


def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        return

    # Set encoding explicitly to handle special characters correctly
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    all_books = []
    for book in books:
        title = book.h3.a["title"]
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = float(price_text[1:])
        all_books.append(
            {
                "title": title,
                "price": price,
                "currency": currency,
            }
        )
    return all_books


all_books = scrape_books(url)

with open("books.json", "w", encoding="utf-8") as f:
    
    json.dump(all_books, f, ensure_ascii=False, indent=4)


with open("books.csv", "w") as f:
   
    
    writer = csv.DictWriter(f, fieldnames=["title", "price", "currency"])
    writer.writeheader()
    writer.writerows(all_books)