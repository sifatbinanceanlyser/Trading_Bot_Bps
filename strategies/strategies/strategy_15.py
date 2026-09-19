import pandas as pd

def check_strategy_15(df):
    """
    Setup - 15: Support False Breakdown Reversal Setup (UP Signal)
    
    Sequence:
    1. Support Box (1): Minimum 2 to maximum 3 consecutive RED candles forming a support baseline.
    2. Bounce Back: Market moves up (at least 1 or 2 GREEN/upward candles).
    3. Candle 2 (r_break): A RED candle that breaks and closes below the Box 1 support level.
    """
    if len(df) < 6:
        return None

    # Candle 2 (The breakdown candle) is the last completed candle
    r_break = df.iloc[-1]
    
    # 1. Check if Candle 2 is RED
    if r_break['close'] >= r_break['open']:
        return None

    # 2. Identify Box 1 (2 or 3 RED candles) and define Support Level
    # Look back past the pullback/bounce candles to locate the support box
    box_candles = []
    support_level = None

    # Dynamically find the Box 1 Support from historical candles
    # Checking for 2 to 3 consecutive red candles in the prior window
    for idx in range(3, min(10, len(df))):
        c1 = df.iloc[-idx]
        c2 = df.iloc[-(idx + 1)]
        
        if c1['close'] < c1['open'] and c2['close'] < c2['open']:
            # Found at least 2 consecutive red candles forming the box
            box_candles = [c1, c2]
            c3 = df.iloc[-(idx + 2)] if (idx + 2) <= len(df) else None
            if c3 is not None and c3['close'] < c3['open']:
                box_candles.append(c3)
            
            # Support is defined by the lowest close/low of the box candles
            support_level = min(c['close'] for c in box_candles)
            break

    if support_level is None:
        return None

    # 3. Check if Candle 2 (r_break) closes BELOW the Box 1 support level
    is_support_broken = r_break['close'] < support_level

    # Final Signal Decision
    if is_support_broken:
        return "CALL"  # Reversal Setup: Next candle UP signal

    return None
          
