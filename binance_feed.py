import pandas as pd
from binance.client import Client

# আপনার Binance API Key ও Secret Code এখানে বসাবেন
BINANCE_API_KEY = "3Xw5chXc4kSXeCP3MoKatiA7IIEBpqTc22UMTiFDoxqfOwffls2WuK7WWhRPFMdK"
BINANCE_API_SECRET = "lUTKnAI5HYbktEN4TS6lNSvzO64G3X6JA9qlgDOVioDgE2yBmqEYwiAWF4VPK6mf"

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
      
