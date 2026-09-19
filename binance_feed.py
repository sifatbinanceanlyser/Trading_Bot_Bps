import pandas as pd
from binance.client import Client

# আপনার Binance API Key ও Secret Code এখানে বসাবেন
BINANCE_API_KEY = "9fugGOQk9vcXLyozou2U8mAnMotyeEB8rBvwxHb2vdu81EIBXSuvYUbrT46TOfqe"
BINANCE_API_SECRET = "VS5c6wCE507foCkLe0NiuLOugxObY558jIDT97SfSA35p5tvxhHvuFZqd9DlCK7x"

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

def get_binance_candles(symbol="EURUSDT", interval=Client.KLINE_INTERVAL_1MINUTE, limit=20):
    """
    Binance থেকে রিয়েল Non-OTC ক্যান্ডেল ডেটা আনে
    """
    try:
        klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
        
        data = []
        for k in klines:
            data.append({
                "time": k[0],
                "open": float(k[1]),
                "high": float(k[2]),
                "low": float(k[3]),
                "close": float(k[4]),
                "volume": float(k[5])
            })
            
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        print(f"Binance API Error: {e}")
        return None
      
