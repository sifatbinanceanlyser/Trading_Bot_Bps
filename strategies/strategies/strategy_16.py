import pandas as pd

def check_strategy_16(df):
    """
    Setup - 16: Resistance False Breakout Reversal Setup (DOWN Signal)
    
    Sequence:
    1. Resistance Box (1): Minimum 2 to maximum 3 consecutive GREEN candles forming a resistance level.
    2. Pullback: Market moves down (at least 1 or 2 RED/downward candles).
    3. Candle 2 (g_break): A GREEN candle that breaks and closes strictly above the Box 1 resistance level.
    """
    if len(df) < 6:
        return None

    # Candle 2 (The breakout candle) is the last completed candle
    g_break = df.iloc[-1]
    
    # 1. Check if Candle 2 is GREEN
    if g_break['close'] <= g_break['open']:
        return None

    # 2. Identify Box 1 (2 or 3 GREEN candles) and define Resistance Level
    box_candles = []
    resistance_level = None

    # Dynamically find the Box 1 Resistance from historical candles
    for idx in range(3, min(10, len(df))):
        c1 = df.iloc[-idx]
        c2 = df.iloc[-(idx + 1)]
        
        if c1['close'] > c1['open'] and c2['close'] > c2['open']:
            # Found at least 2 consecutive green candles forming the box
            box_candles = [c1, c2]
            c3 = df.iloc[-(idx + 2)] if (idx + 2) <= len(df) else None
            if c3 is not None and c3['close'] > c3['open']:
                box_candles.append(c3)
            
            # Resistance is defined by the highest close/high of the box candles
            resistance_level = max(c['close'] for c in box_candles)
            break

    if resistance_level is None:
        return None

    # 3. Check if Candle 2 (g_break) closes ABOVE the Box 1 resistance level
    is_resistance_broken = g_break['close'] > resistance_level

    # Final Signal Decision
    if is_resistance_broken:
        return "PUT"  # Reversal Setup: Next candle DOWN signal

    return None
  
