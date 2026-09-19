import pandas as pd

def check_strategy_20(df):
    """
    Setup - 20: Bearish Continuation Inside Candle Setup (PUT Signal)
    
    Sequence:
    1. Overall Downtrend (prior RED candles).
    2. Candle 1 (c1): A GREEN pullback candle.
    3. Candle 2 (c2): A RED candle that closes inside Candle 1's body/range without breaking it.
    """
    if len(df) < 4:
        return None

    # Extract relevant candles
    prior_red = df.iloc[-3]  # Prior RED candle confirming downtrend
    c1 = df.iloc[-2]         # 1-no GREEN candle
    c2 = df.iloc[-1]         # 2-no RED candle

    # 1. Check Colors
    is_prior_red = prior_red['close'] < prior_red['open']
    is_c1_green = c1['close'] > c1['open']
    is_c2_red = c2['close'] < c2['open']

    if not (is_prior_red and is_c1_green and is_c2_red):
        return None

    # 2. Check if Candle 2 stays inside Candle 1's body and does not break its Low
    # Candle 1 Open is bottom of body, Close is top of body
    c1_body_bottom = c1['open']
    c1_body_top = c1['close']

    # Candle 2 close must be strictly inside Candle 1 body range
    closes_inside_c1 = (c2['close'] > c1_body_bottom) and (c2['close'] < c1_body_top)
    
    # Candle 2 does not break Candle 1's lowest price (Low)
    does_not_break_low = c2['low'] >= c1['low']

    # Final Signal Decision
    if closes_inside_c1 and does_not_break_low:
        return "PUT"  # Continuation Setup: Next candle DOWN signal

    return None
  
