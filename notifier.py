
import requests

TOKEN = "7646161458:AAGh-G0BJKQFTnQHswLePdBUXhrtuJsPe8M"
CHAT_ID = "@ibocellkampanya"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, data=data)
        if response.status_code != 200:
            print(f"Telegram mesaj hatası: {response.text}")
    except Exception as e:
        print(f"❌ Telegram bağlantı hatası: {e}")
