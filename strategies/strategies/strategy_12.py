import pandas as pd

def check_strategy_12(df):
    """
    Setup - 12: Support Breakdown Re-test Reversal (DOWN Signal)
    
    Sequence:
    1. Candle 1 (g1): Normal GREEN candle.
    2. Candle 2 (g2): Small GREEN candle with both upper and lower wicks.
    3. Candle 3 (r3): RED candle that breaks below Candle 1 Open (Support).
    4. Candle 4 (g4): Small GREEN candle touching Support (High >= g1 Open) and closing BELOW Support (Close < g1 Open).
    """
    if len(df) < 4:
        return None

    g1 = df.iloc[-4]  # 1-no Normal Green Candle
    g2 = df.iloc[-3]  # 2-no Small Green Candle with wicks
    r3 = df.iloc[-2]  # 3-no Red Breakdown Candle
    g4 = df.iloc[-1]  # 4-no Small Green Re-test Candle

    # SNR Support Level is defined by Candle 1 Open
    snr_support = g1['open']

    # 1. Color Checks
    is_g1_green = g1['close'] > g1['open']
    is_g2_green = g2['close'] > g2['open']
    is_r3_red = r3['close'] < r3['open']
    is_g4_green = g4['close'] > g4['open']

    colors_ok = is_g1_green and is_g2_green and is_r3_red and is_g4_green

    # 2. Candle 2 Wick Check (Has both upper and lower wicks)
    has_upper_wick_2 = g2['high'] > max(g2['open'], g2['close'])
    has_lower_wick_2 = g2['low'] < min(g2['open'], g2['close'])
    g2_wicks_ok = has_upper_wick_2 and has_lower_wick_2

    # 3. Candle 3 Breakdown (Closes below Candle 1 Open / Support)
    r3_breaks_snr = r3['close'] < snr_support

    # 4. Candle 4 Re-test (Touches SNR with High wick and Closes BELOW SNR)
    g4_touches_snr = g4['high'] >= snr_support
    g4_closes_below_snr = g4['close'] < snr_support

    # Final Decision
    if colors_ok and g2_wicks_ok and r3_breaks_snr and g4_touches_snr and g4_closes_below_snr:
        return "PUT"  # Next candle DOWN signal

    return None
  
