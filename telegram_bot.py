import requests

TELEGRAM_BOT_TOKEN = "8953696893:AAGW7gCQ305bxhGuWuriIOQvezpTHriOzjA"
TELEGRAM_CHAT_ID = "6885238220"

def send_telegram_signal(symbol, setup_name, signal_type):
    emoji = "🟢 CALL (UP)" if signal_type == "CALL" else "🔴 PUT (DOWN)"
    
    message = (
        f"🚨 **NEW TRADING SIGNAL (Non-OTC)** 🚨\n\n"
        f"📊 **Asset:** {symbol}\n"
        f"🎯 **Strategy:** {setup_name}\n"
        f"⚡ **Direction:** {emoji}\n"
        f"⏱ **Timeframe:** 1 Minute\n\n"
        f"⚠️ *Quotex-এ ক্যান্ডেল শুরু হওয়ার ১-২ সেকেন্ড আগে ট্রেড প্লেস করুন!*"
    )
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Telegram Alert Error: {e}")
      
