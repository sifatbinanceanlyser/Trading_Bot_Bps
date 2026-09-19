import pandas as pd

def check_strategy_14(df, snr_support):
    """
    Setup - 14: Support Breakdown & Re-test Continuation Setup (DOWN Signal)
    
    Sequence:
    1. Downtrend check: Prior red candles moving downward.
    2. Candle 1 (r1): RED breakdown candle closing strictly below SNR support.
    3. Candle 2 (g2): GREEN re-test candle touching SNR support (High >= snr_support) 
       and closing strictly below SNR support (Close < snr_support).
    """
    if len(df) < 4:
        return None

    # Getting relevant candles
    p2 = df.iloc[-4]  # Prior Trend Red Candle 1
    p1 = df.iloc[-3]  # Prior Trend Red Candle 2
    r1 = df.iloc[-2]  # 1-no Red Breakdown Candle
    g2 = df.iloc[-1]  # 2-no Green Re-test Candle

    # 1. Prior Downtrend Check (2 Red Candles before breakdown)
    is_p2_red = p2['close'] < p2['open']
    is_p1_red = p1['close'] < p1['open']
    prior_downtrend = is_p2_red and is_p1_red and (p1['close'] < p2['close'])

    # 2. Color Checks for Breakdown and Re-test Candles
    is_r1_red = r1['close'] < r1['open']
    is_g2_green = g2['close'] > g2['open']

    # 3. Breakdown Condition (Candle 1 closes below SNR support)
    r1_breaks_snr = r1['close'] < snr_support

    # 4. Re-test Condition (Candle 2 touches SNR with High wick and closes below SNR)
    g2_touches_snr = g2['high'] >= snr_support
    g2_closes_below_snr = g2['close'] < snr_support

    # Final Decision
    if (prior_downtrend and is_r1_red and is_g2_green and 
        r1_breaks_snr and g2_touches_snr and g2_closes_below_snr):
        return "PUT"  # Next candle DOWN signal

    return None
  
