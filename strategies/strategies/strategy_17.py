import pandas as pd

def check_strategy_17(df):
    """
    Setup - 17: Momentum Loss Bullish Engulfing Reversal (CALL Signal)
    
    Sequence:
    1. Candles 1, 2, 3 are RED candles moving downward.
    2. Candle body sizes are progressively decreasing (c1_body > c2_body > c3_body).
    3. Candle 4 is a GREEN candle that completely engulfs Candle 3's body.
    """
    if len(df) < 4:
        return None

    # Extract last 4 candles
    c1 = df.iloc[-4] # 1-no Red
    c2 = df.iloc[-3] # 2-no Red
    c3 = df.iloc[-2] # 3-no Red
    c4 = df.iloc[-1] # 4-no Green Engulfing

    # 1. Color Checks
    is_c1_red = c1['close'] < c1['open']
    is_c2_red = c2['close'] < c2['open']
    is_c3_red = c3['close'] < c3['open']
    is_c4_green = c4['close'] > c4['open']

    if not (is_c1_red and is_c2_red and is_c3_red and is_c4_green):
        return None

    # 2. Calculate Body Sizes (Absolute values)
    c1_body = abs(c1['open'] - c1['close'])
    c2_body = abs(c2['open'] - c2['close'])
    c3_body = abs(c3['open'] - c3['close'])

    # 3. Check Progressive Size Decreasing (1 > 2 > 3)
    is_size_decreasing = (c1_body > c2_body) and (c2_body > c3_body)

    # 4. Check Bullish Engulfing Condition (Candle 4 engulfs Candle 3 body)
    # Candle 4 Open is below/equal to Candle 3 Close AND Candle 4 Close is above Candle 3 Open
    is_engulfing = (c4['open'] <= c3['close']) and (c4['close'] > c3['open'])

    # Final Signal Decision
    if is_size_decreasing and is_engulfing:
        return "CALL"  # Next candle UP signal

    return None
  
