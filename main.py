import requests
from bs4 import BeautifulSoup
import csv

def extract_product_info(url):
    """
    Extract product names and prices from the given URL
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        product_names = soup.find_all("span", attrs={"role": "heading", "aria-level": "3"})
        product_prices = soup.find_all('span', class_='s-item__price')

        with open('product_info.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Product Name', 'Product Price'])
            for name, price in zip(product_names, product_prices):
                writer.writerow([name.text, price.text])
    except Exception as e:
        print(f"Error occured: {e}")

URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=ps5&_sacat=0"
extract_product_info(URL)
