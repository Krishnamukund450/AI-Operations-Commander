import requests

BOT_TOKEN = "Paste Your Telegram Token Here"
CHAT_ID = "2032396652"

def send_alert(message):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        requests.post(url, json={
            "chat_id": CHAT_ID,
            "text": message
        })

        print("📩 Alert sent to Telegram")

    except Exception as e:
        print("Alert failed:", e)
