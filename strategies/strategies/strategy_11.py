import pandas as pd

def check_strategy_11(df):
    """
    Setup - 11: Re-test Reversal after SNR Breakout (UP Signal)
    
    Sequence:
    1. Candle 1 (r1): Normal RED candle.
    2. Candle 2 (r2): Small RED candle with both top and bottom wicks.
    3. Candle 3 (g3): GREEN candle that breaks above Candle 1 Open (Resistance).
    4. Candle 4 (r4): Small RED candle touching Resistance (Low <= r1 Open) and closing ABOVE Resistance (Close > r1 Open).
    """
    if len(df) < 4:
        return None

    r1 = df.iloc[-4]  # 1-no Normal Red Candle
    r2 = df.iloc[-3]  # 2-no Small Red Candle with wicks
    g3 = df.iloc[-2]  # 3-no Green Breakout Candle
    r4 = df.iloc[-1]  # 4-no Small Red Re-test Candle

    # SNR Resistance Level is defined by Candle 1 Open
    snr_resistance = r1['open']

    # 1. Color Checks
    is_r1_red = r1['close'] < r1['open']
    is_r2_red = r2['close'] < r2['open']
    is_g3_green = g3['close'] > g3['open']
    is_r4_red = r4['close'] < r4['open']

    colors_ok = is_r1_red and is_r2_red and is_g3_green and is_r4_red

    # 2. Candle 2 Wick Check (Has both upper and lower wicks)
    has_upper_wick_2 = r2['high'] > max(r2['open'], r2['close'])
    has_lower_wick_2 = r2['low'] < min(r2['open'], r2['close'])
    r2_wicks_ok = has_upper_wick_2 and has_lower_wick_2

    # 3. Candle 3 Breakout (Closes above Candle 1 Open / Resistance)
    g3_breaks_snr = g3['close'] > snr_resistance

    # 4. Candle 4 Re-test (Touches SNR with Low wick and Closes ABOVE SNR)
    r4_touches_snr = r4['low'] <= snr_resistance
    r4_closes_above_snr = r4['close'] > snr_resistance

    # Final Decision
    if colors_ok and r2_wicks_ok and g3_breaks_snr and r4_touches_snr and r4_closes_above_snr:
        return "CALL"  # Next candle UP signal

    return None
  
