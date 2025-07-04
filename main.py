
import time
import schedule
from scraper import get_products_from_category
from tracker import check_price_changes

CATEGORIES = {
    "Cep Telefonu": "https://www.mediamarkt.com.tr/tr/category/_cep-telefonu-504307.html",
    "Laptop": "https://www.mediamarkt.com.tr/tr/category/_notebook-504324.html",
    "Tablet": "https://www.mediamarkt.com.tr/tr/category/_tablet-504308.html",
    "Akıllı Saat": "https://www.mediamarkt.com.tr/tr/category/_akilli-saat-647162.html"
}

def run_bot():
    print("🔄 Fiyatlar kontrol ediliyor...")
    all_products = []
    for category, url in CATEGORIES.items():
        products = get_products_from_category(category, url)
        all_products.extend(products)

    check_price_changes(all_products)

schedule.every(10).minutes.do(run_bot)

# İlk başta bir kez çalıştır
run_bot()

# Sonsuz döngü
while True:
    schedule.run_pending()
    time.sleep(1)
