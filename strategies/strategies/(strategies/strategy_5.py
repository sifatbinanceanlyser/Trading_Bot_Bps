import pandas as pd

def check_strategy_5(df, snr_support_level):
    """
    Setup - 5: Support Doji Reversal Setup (UP Signal)
    """
    if len(df) < 5:
        return None

    candle_1 = df.iloc[-1]  # Latest completed Doji candle

    # 1. Market Niche Jawyar Logic (Strict Downtrend Check)
    # Dekha hochhe purborobi 3-ti candle-er proti ti porer candle ager candle-er niche close hoyeche kina
    p1 = df.iloc[-4]
    p2 = df.iloc[-3]
    p3 = df.iloc[-2]
    
    is_downtrend = (p1['close'] < p1['open']) and (p2['close'] < p2['open']) and (p3['close'] < p3['open'])

    # 2. Doji Candle Logic (Body size total range-er <= 10%)
    body_size = abs(candle_1['close'] - candle_1['open'])
    total_range = candle_1['high'] - candle_1['low']
    total_range = 0.00001 if total_range == 0 else total_range  # Zero division fix
    
    is_doji = (body_size / total_range) <= 0.10

    # 3. SNR Touch & Close Above Support Logic
    touches_snr_1 = candle_1['low'] <= snr_support_level
    closes_above_snr_1 = candle_1['close'] > snr_support_level

    # Sob condition match korle Signal: UP (CALL)
    if is_downtrend and is_doji and touches_snr_1 and closes_above_snr_1:
        return "CALL"

    return None
  
