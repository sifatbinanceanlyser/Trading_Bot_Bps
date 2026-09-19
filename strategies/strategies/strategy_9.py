import pandas as pd

def check_strategy_9(df):
    """
    Setup - 9: Red Candle + Two Green + Large Red Engulfing Reversal (UP Signal)
    
    Sequence:
    1. Candle 0 (r0): Prior RED candle before green push.
    2. Candle 1 (g1) & Candle 2 (g2): Two consecutive GREEN candles.
    3. Candle 3 (r3): RED candle that engulfs both green candles (Closes below g1 Open).
    """
    if len(df) < 4:
        return None

    # Getting last 4 candles
    r0 = df.iloc[-4]  # Prior Red Candle
    g1 = df.iloc[-3]  # 1st Green Candle (inside box 1)
    g2 = df.iloc[-2]  # 2nd Green Candle (inside box 1)
    r3 = df.iloc[-1]  # Large Red Candle (Candle 2)

    # 1. Color Checks
    is_r0_red = r0['close'] < r0['open']
    is_g1_green = g1['close'] > g1['open']
    is_g2_green = g2['close'] > g2['open']
    is_r3_red = r3['close'] < r3['open']

    correct_sequence = is_r0_red and is_g1_green and is_g2_green and is_r3_red

    # 2. Engulfing Condition: Red candle 3 closes below the lowest Open of the two green candles
    lowest_green_open = min(g1['open'], g2['open'])
    engulfs_both = r3['close'] < lowest_green_open

    # Final Decision
    if correct_sequence and engulfs_both:
        return "CALL"  # Next candle UP signal

    return None
    
