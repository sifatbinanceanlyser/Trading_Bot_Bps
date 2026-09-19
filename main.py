import time
from datetime import datetime
from binance_feed import get_binance_candles
from telegram_bot import send_telegram_signal

# strategies/strategies folder theke 20-ti strategy import kora
from strategies.strategies.strategy_1 import check_strategy_1
from strategies.strategies.strategy_2 import check_strategy_2
from strategies.strategies.strategy_3 import check_strategy_3
from strategies.strategies.strategy_4 import check_strategy_4
from strategies.strategies.strategy_5 import check_strategy_5
from strategies.strategies.strategy_6 import check_strategy_6
from strategies.strategies.strategy_7 import check_strategy_7
from strategies.strategies.strategy_8 import check_strategy_8
from strategies.strategies.strategy_9 import check_strategy_9
from strategies.strategies.strategy_10 import check_strategy_10
from strategies.strategies.strategy_11 import check_strategy_11
from strategies.strategies.strategy_12 import check_strategy_12
from strategies.strategies.strategy_13 import check_strategy_13
from strategies.strategies.strategy_14 import check_strategy_14
from strategies.strategies.strategy_15 import check_strategy_15
from strategies.strategies.strategy_16 import check_strategy_16
from strategies.strategies.strategy_17 import check_strategy_17
from strategies.strategies.strategy_18 import check_strategy_18
from strategies.strategies.strategy_19 import check_strategy_19
from strategies.strategies.strategy_20 import check_strategy_20

STRATEGY_LIST = [
    ("Setup 1", check_strategy_1), ("Setup 2", check_strategy_2),
    ("Setup 3", check_strategy_3), ("Setup 4", check_strategy_4),
    ("Setup 5", check_strategy_5), ("Setup 6", check_strategy_6),
    ("Setup 7", check_strategy_7), ("Setup 8", check_strategy_8),
    ("Setup 9", check_strategy_9), ("Setup 10", check_strategy_10),
    ("Setup 11", check_strategy_11), ("Setup 12", check_strategy_12),
    ("Setup 13", check_strategy_13), ("Setup 14", check_strategy_14),
    ("Setup 15", check_strategy_15), ("Setup 16", check_strategy_16),
    ("Setup 17", check_strategy_17), ("Setup 18", check_strategy_18),
    ("Setup 19", check_strategy_19), ("Setup 20", check_strategy_20)
]

# Quotex Non-OTC match korar moto shobgulo major forex ebong crypto pair-er list
PAIRS = [
    # Major Forex & Cross Pairs (Binance USDT Pairs)
    "EURUSDT",
    "GBPUSDT",
    "AUDUSDT",
    "USDCAD",
    "USDJPY",
    "EURJPY",
    "GBPJPY",
    "NZDUSDT",
    "AUDJPY",
    "EURGBP",
    "EURAUD",
    "GBPAUD",
    "CHFJPY",
    "CADJPY",
    "AUDCAD",
    
    # Popular Crypto Pairs (Binance Spot)
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "XRPUSDT",
    "ADAUSDT",
    "DOGEUSDT"
]

def scan_all_strategies(df):
    for setup_name, func in STRATEGY_LIST:
        try:
            signal = func(df)
            if signal in ["CALL", "PUT"]:
                return setup_name, signal
        except Exception:
            continue
    return None, None

def start_bot():
    print("🤖 24/7 Binance Non-OTC Scanning Bot Started...")
    last_scanned_minute = -1

    while True:
        now = datetime.now()
        second = now.second
        minute = now.minute

        # Proti minute-er thik 58-th second-e scan korbe
        if second == 58 and minute != last_scanned_minute:
            last_scanned_minute = minute
            print(f"\n🔍 Scanning Market at {now.strftime('%H:%M:%S')}...")

            for symbol in PAIRS:
                df = get_binance_candles(symbol=symbol)
                
                if df is not None and not df.empty:
                    setup_name, signal = scan_all_strategies(df)
                    
                    if signal:
                        print(f"✅ MATCH FOUND! [{symbol}] - {setup_name} -> {signal}")
                        send_telegram_signal(symbol, setup_name, signal)
            
            time.sleep(3)

        time.sleep(0.5)

if __name__ == "__main__":
    start_bot()
    
