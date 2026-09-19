import pandas as pd

def check_strategy_10(df):
    """
    Setup - 10: Prior Green + Two Red + Large Green Engulfing Reversal (DOWN Signal)
    
    Sequence:
    1. Candle 0 (g0): Prior GREEN candle before red push.
    2. Candle 1 (r1) & Candle 2 (r2): Two consecutive RED candles (inside box 1).
    3. Candle 3 (g3): GREEN candle that engulfs both red candles (Closes strictly above r1 Open).
    """
    if len(df) < 4:
        return None

    # Getting last 4 candles
    g0 = df.iloc[-4]  # Prior Green Candle
    r1 = df.iloc[-3]  # 1st Red Candle (inside box 1)
    r2 = df.iloc[-2]  # 2nd Red Candle (inside box 1)
    g3 = df.iloc[-1]  # Large Green Candle (Candle 2)

    # 1. Color Checks
    is_g0_green = g0['close'] > g0['open']
    is_r1_red = r1['close'] < r1['open']
    is_r2_red = r2['close'] < r2['open']
    is_g3_green = g3['close'] > g3['open']

    correct_sequence = is_g0_green and is_r1_red and is_r2_red and is_g3_green

    # 2. Engulfing Condition: Green candle 3 closes above the highest Open of the two red candles
    highest_red_open = max(r1['open'], r2['open'])
    engulfs_both = g3['close'] > highest_red_open

    # Final Decision
    if correct_sequence and engulfs_both:
        return "PUT"  # Next candle DOWN signal

    return None
  
