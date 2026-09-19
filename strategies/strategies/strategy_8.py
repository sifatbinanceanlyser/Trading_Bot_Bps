import pandas as pd

def check_strategy_8(df, snr_support_level):
    """
    Setup - 8: Support Breakdown Re-test Reversal (DOWN Signal)
    
    Conditions:
    1. Strict Downtrend: Prior 3 candles are RED and making lower closes.
    2. Candle 1: RED breakdown candle (Closes below SNR support).
    3. Candle 2: Small RED candle below SNR support.
    4. Candle 3: GREEN candle that engulfs Candle 2.
    5. Candle 3 High touches SNR (High >= SNR) and Closes strictly BELOW SNR (Close < SNR).
    """
    if len(df) < 7:
        return None

    # Candle references
    p3 = df.iloc[-6]        # Trend Candle 1
    p2 = df.iloc[-5]        # Trend Candle 2
    p1 = df.iloc[-4]        # Trend Candle 3
    candle_1 = df.iloc[-3]  # 1-no Red Breakdown Candle
    candle_2 = df.iloc[-2]  # 2-no Red Candle
    candle_3 = df.iloc[-1]  # 3-no Green Re-test Candle

    # 1. Strict Market Downtrend Check (3 consecutive RED candles moving DOWN)
    is_p3_red = p3['close'] < p3['open']
    is_p2_red = p2['close'] < p2['open']
    is_p1_red = p1['close'] < p1['open']
    
    is_making_lower_closes = (p1['close'] < p2['close']) and (p2['close'] < p3['close'])
    
    strict_downtrend = is_p3_red and is_p2_red and is_p1_red and is_making_lower_closes

    # 2. Candle 1: RED & Breaks SNR Support
    is_c1_red = candle_1['close'] < candle_1['open']
    c1_breaks_snr = candle_1['close'] < snr_support_level

    # 3. Candle 2: RED & Below SNR Support
    is_c2_red = candle_2['close'] < candle_2['open']
    c2_below_snr = candle_2['open'] <= snr_support_level

    # 4. Candle 3: GREEN & Engulfs Candle 2
    is_c3_green = candle_3['close'] > candle_3['open']
    engulfs_c2 = (candle_3['open'] <= candle_2['close']) and (candle_3['close'] >= candle_2['open'])

    # 5. Candle 3 SNR Touch with Upper Wick & Closes BELOW SNR Support
    touches_snr_3 = candle_3['high'] >= snr_support_level
    closes_below_snr_3 = candle_3['close'] < snr_support_level

    # Final Decision
    if (strict_downtrend and is_c1_red and c1_breaks_snr and 
        is_c2_red and c2_below_snr and 
        is_c3_green and engulfs_c2 and touches_snr_3 and closes_below_snr_3):
        return "PUT"  # Next candle DOWN signal

    return None
  
