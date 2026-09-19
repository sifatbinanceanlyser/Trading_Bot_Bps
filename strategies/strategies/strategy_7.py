import pandas as pd

def check_strategy_7(df, snr_resistance_level):
    """
    Setup - 7: SNR Breakout Re-test Reversal (UP Signal)
    
    Conditions:
    1. Strict Uptrend: Prior 3 candles are GREEN and making higher closes.
    2. Candle 1: GREEN breakout candle (Closes above SNR).
    3. Candle 2: Small GREEN candle above SNR.
    4. Candle 3: RED candle that engulfs Candle 2.
    5. Candle 3 Low touches SNR (Low <= SNR) and Closes strictly ABOVE SNR (Close > SNR).
    """
    if len(df) < 7:
        return None

    # Candle references
    p3 = df.iloc[-6]        # Trend Candle 1
    p2 = df.iloc[-5]        # Trend Candle 2
    p1 = df.iloc[-4]        # Trend Candle 3
    candle_1 = df.iloc[-3]  # 1-no Green Breakout Candle
    candle_2 = df.iloc[-2]  # 2-no Green Candle
    candle_3 = df.iloc[-1]  # 3-no Red Re-test Candle

    # 1. Strict Market Uptrend Check (3 consecutive GREEN candles moving UP)
    is_p3_green = p3['close'] > p3['open']
    is_p2_green = p2['close'] > p2['open']
    is_p1_green = p1['close'] > p1['open']
    
    is_making_higher_closes = (p1['close'] > p2['close']) and (p2['close'] > p3['close'])
    
    strict_uptrend = is_p3_green and is_p2_green and is_p1_green and is_making_higher_closes

    # 2. Candle 1: GREEN & Breaks SNR
    is_c1_green = candle_1['close'] > candle_1['open']
    c1_breaks_snr = candle_1['close'] > snr_resistance_level

    # 3. Candle 2: GREEN & Above SNR
    is_c2_green = candle_2['close'] > candle_2['open']
    c2_above_snr = candle_2['open'] >= snr_resistance_level

    # 4. Candle 3: RED & Engulfs Candle 2
    is_c3_red = candle_3['close'] < candle_3['open']
    engulfs_c2 = (candle_3['open'] >= candle_2['close']) and (candle_3['close'] <= candle_2['open'])

    # 5. Candle 3 SNR Touch with Wick & Closes ABOVE SNR
    touches_snr_3 = candle_3['low'] <= snr_resistance_level
    closes_above_snr_3 = candle_3['close'] > snr_resistance_level

    # Final Decision
    if (strict_uptrend and is_c1_green and c1_breaks_snr and 
        is_c2_green and c2_above_snr and 
        is_c3_red and engulfs_c2 and touches_snr_3 and closes_above_snr_3):
        return "CALL"  # Next candle UP signal

    return None
  
