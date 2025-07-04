
import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_products_from_category(category_name, url):
    products = []
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        product_elements = soup.select(".product-wrapper")

        for product in product_elements:
            title_tag = product.select_one(".product-title")
            price_tag = product.select_one(".price")

            if not title_tag or not price_tag:
                continue

            name = title_tag.get_text(strip=True)
            price = price_tag.get_text(strip=True)

            products.append({
                "category": category_name,
                "name": name,
                "price": price
            })

    except Exception as e:
        print(f"⚠️ Hata ({category_name}): {e}")

    return products
