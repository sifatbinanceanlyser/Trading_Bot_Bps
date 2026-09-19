import pandas as pd

def check_strategy_9(df):
    """
    Setup - 9: Two Green Engulfed by Large Red (UP Signal)
    
    Conditions:
    1. Candle 1 & Candle 2: Two consecutive GREEN candles.
    2. Candle 3: RED candle.
    3. Candle 3 Closes strictly BELOW the Open of Candle 1 (engulfs both green candles).
    """
    if len(df) < 3:
        return None

    # Getting last 3 candles
    g1 = df.iloc[-3]  # First Green Candle (inside box 1)
    g2 = df.iloc[-2]  # Second Green Candle (inside box 1)
    r3 = df.iloc[-1]  # Large Red Candle (Candle 2)

    # 1. Color Checks
    is_g1_green = g1['close'] > g1['open']
    is_g2_green = g2['close'] > g2['open']
    is_r3_red = r3['close'] < r3['open']

    both_green = is_g1_green and is_g2_green

    # 2. Engulfing Condition: Red candle closes below the lowest point/open of the 1st green candle
    lowest_green_open = min(g1['open'], g2['open'])
    engulfs_both = r3['close'] < lowest_green_open

    # Final Decision
    if both_green and is_r3_red and engulfs_both:
        return "CALL"  # Next candle UP signal

    return None
  
