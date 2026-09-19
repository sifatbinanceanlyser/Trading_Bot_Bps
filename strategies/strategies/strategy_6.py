import pandas as pd

def check_strategy_6(df, snr_resistance_level):
    """
    Setup - 6: Resistance Doji Reversal Setup (DOWN Signal)
    
    Conditions:
    1. Uptrend: Market is moving upwards before Candle 1.
    2. Candle 1: Doji Candle (Open and Close are almost equal, very small body).
    3. Touches Resistance: High >= SNR resistance level.
    4. Closes Below Resistance: Close < SNR resistance level.
    """
    if len(df) < 5:
        return None

    candle_1 = df.iloc[-1]  # Latest completed Doji candle

    # 1. Strict Uptrend Check (Prior 3 candles are GREEN and moving up)
    p1 = df.iloc[-4]
    p2 = df.iloc[-3]
    p3 = df.iloc[-2]
    
    is_uptrend = (p1['close'] > p1['open']) and (p2['close'] > p2['open']) and (p3['close'] > p3['open'])

    # 2. Doji Candle Logic (Body size <= 10% of total range)
    body_size = abs(candle_1['close'] - candle_1['open'])
    total_range = candle_1['high'] - candle_1['low']
    total_range = 0.00001 if total_range == 0 else total_range  # Avoid zero division
    
    is_doji = (body_size / total_range) <= 0.10

    # 3. SNR Touch & Close Below Resistance Logic
    touches_snr_1 = candle_1['high'] >= snr_resistance_level
    closes_below_snr_1 = candle_1['close'] < snr_resistance_level

    # Final Signal Decision
    if is_uptrend and is_doji and touches_snr_1 and closes_below_snr_1:
        return "PUT"  # Next candle DOWN signal

    return None
  
