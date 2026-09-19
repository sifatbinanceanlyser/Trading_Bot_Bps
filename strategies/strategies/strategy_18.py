import pandas as pd

def check_strategy_18(df):
    """
    Setup - 18: Momentum Loss Bearish Engulfing Reversal (PUT Signal)
    
    Sequence:
    1. Candles 1, 2, 3 are GREEN candles moving upward.
    2. Candle body sizes are progressively decreasing (c1_body > c2_body > c3_body).
    3. Candle 4 is a RED candle that completely engulfs Candle 3's body.
    """
    if len(df) < 4:
        return None

    # Extract last 4 candles
    c1 = df.iloc[-4] # 1-no Green
    c2 = df.iloc[-3] # 2-no Green
    c3 = df.iloc[-2] # 3-no Green
    c4 = df.iloc[-1] # 4-no Red Engulfing

    # 1. Color Checks
    is_c1_green = c1['close'] > c1['open']
    is_c2_green = c2['close'] > c2['open']
    is_c3_green = c3['close'] > c3['open']
    is_c4_red = c4['close'] < c4['open']

    if not (is_c1_green and is_c2_green and is_c3_green and is_c4_red):
        return None

    # 2. Calculate Body Sizes (Absolute values)
    c1_body = abs(c1['close'] - c1['open'])
    c2_body = abs(c2['close'] - c2['open'])
    c3_body = abs(c3['close'] - c3['open'])

    # 3. Check Progressive Size Decreasing (1 > 2 > 3)
    is_size_decreasing = (c1_body > c2_body) and (c2_body > c3_body)

    # 4. Check Bearish Engulfing Condition (Candle 4 engulfs Candle 3 body)
    # Candle 4 Open is above/equal to Candle 3 Close AND Candle 4 Close is below Candle 3 Open
    is_engulfing = (c4['open'] >= c3['close']) and (c4['close'] < c3['open'])

    # Final Signal Decision
    if is_size_decreasing and is_engulfing:
        return "PUT"  # Next candle DOWN signal

    return None
  
