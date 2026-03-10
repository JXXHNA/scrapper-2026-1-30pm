import requests
from bs4 import BeautifulSoup 

# url of the website to scrape
url = "http://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title=book.h3.a["title"]
        price_text-book.find("p",class_="price_color").text
        currency=price_text[0]
        price=float(price_text[1;])
        print(title,price,currency)
    
    
    scrape_books(url)
