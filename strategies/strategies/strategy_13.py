import pandas as pd

def check_strategy_13(df, snr_resistance):
    """
    Setup - 13: Breakout & Re-test Continuation Setup (UP Signal)
    
    Sequence:
    1. Uptrend check: 2 prior green candles before breakout candle.
    2. Candle 1 (g1): GREEN breakout candle closing above SNR resistance.
    3. Candle 2 (r2): RED re-test candle touching SNR resistance (Low <= snr_resistance) 
       and closing strictly above SNR resistance (Close > snr_resistance).
    """
    if len(df) < 4:
        return None

    # Getting relevant candles
    p2 = df.iloc[-4]  # Prior Trend Green Candle 1
    p1 = df.iloc[-3]  # Prior Trend Green Candle 2
    g1 = df.iloc[-2]  # 1-no Green Breakout Candle
    r2 = df.iloc[-1]  # 2-no Red Re-test Candle

    # 1. Prior Uptrend Check (2 Green Candles before breakout)
    is_p2_green = p2['close'] > p2['open']
    is_p1_green = p1['close'] > p1['open']
    prior_uptrend = is_p2_green and is_p1_green and (p1['close'] > p2['close'])

    # 2. Color Checks for Breakout and Re-test Candles
    is_g1_green = g1['close'] > g1['open']
    is_r2_red = r2['close'] < r2['open']

    # 3. Breakout Condition (Candle 1 closes above SNR resistance)
    g1_breaks_snr = g1['close'] > snr_resistance

    # 4. Re-test Condition (Candle 2 touches SNR with low wick and closes above SNR)
    r2_touches_snr = r2['low'] <= snr_resistance
    r2_closes_above_snr = r2['close'] > snr_resistance

    # Final Decision
    if (prior_uptrend and is_g1_green and is_r2_red and 
        g1_breaks_snr and r2_touches_snr and r2_closes_above_snr):
        return "CALL"  # Next candle UP signal

    return None
  
