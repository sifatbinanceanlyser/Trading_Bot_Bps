import pandas as pd

def check_strategy_19(df):
    """
    Setup - 19: Bullish Continuation Inside Candle Setup (CALL Signal)
    
    Sequence:
    1. Overall Uptrend (prior GREEN candles).
    2. Candle 1 (c1): A RED pullback candle.
    3. Candle 2 (c2): A GREEN candle that closes inside Candle 1's body/range without breaking it.
    """
    if len(df) < 4:
        return None

    # Extract relevant candles
    prior_green = df.iloc[-3] # Prior GREEN candle confirming uptrend
    c1 = df.iloc[-2]         # 1-no RED candle
    c2 = df.iloc[-1]         # 2-no GREEN candle

    # 1. Check Colors
    is_prior_green = prior_green['close'] > prior_green['open']
    is_c1_red = c1['close'] < c1['open']
    is_c2_green = c2['close'] > c2['open']

    if not (is_prior_green and is_c1_red and is_c2_green):
        return None

    # 2. Check if Candle 2 stays inside Candle 1's body and does not break its High
    # Candle 1 Open is the top of body, Close is the bottom of body
    c1_body_top = c1['open']
    c1_body_bottom = c1['close']

    # Candle 2 close must be strictly inside Candle 1 body range
    closes_inside_c1 = (c2['close'] > c1_body_bottom) and (c2['close'] < c1_body_top)
    
    # Candle 2 does not break Candle 1's highest price (High)
    does_not_break_high = c2['high'] <= c1['high']

    # Final Signal Decision
    if closes_inside_c1 and does_not_break_high:
        return "CALL"  # Continuation Setup: Next candle UP signal

    return None
  
