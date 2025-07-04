
import json
from notifier import send_telegram_message

PRICE_FILE = "fiyatlar.json"

try:
    with open(PRICE_FILE, "r") as f:
        old_prices = json.load(f)
except:
    old_prices = {}

def check_price_changes(products):
    global old_prices
    for product in products:
        key = f"{product['category']}::{product['name']}"
        new_price = product["price"]
        old_price = old_prices.get(key)

        if old_price and old_price != new_price:
            message = (
                f"📉 *Fiyat Düştü!*
"
                f"📦 {product['name']}
"
                f"💰 Eski: {old_price}
"
                f"🆕 Yeni: {new_price}
"
                f"📍 Kategori: {product['category']}"
            )
            send_telegram_message(message)

        old_prices[key] = new_price

    with open(PRICE_FILE, "w") as f:
        json.dump(old_prices, f)
