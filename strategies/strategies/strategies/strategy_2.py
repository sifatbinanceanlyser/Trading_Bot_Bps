import pandas as pd

def check_strategy_2(df, snr_support_level):
    """
    Setup - 2: Support Breakout Setup (DOWN Signal)
    
    Conditions:
    1. Downtrend: Market is moving downwards before Candle 1.
    2. Candle 1: GREEN candle. Low <= SNR support level (touches SNR), 
                 but Close > SNR support level (closes above SNR).
    3. Candle 2: RED candle. Closes strictly BELOW SNR support level (Breakout).
    """
    if len(df) < 5:
        return None

    # Candle references
    # df.iloc[-2] = Candle 1 (Previous green candle)
    # df.iloc[-1] = Candle 2 (Latest completed red breakout candle)
    candle_1 = df.iloc[-2]
    candle_2 = df.iloc[-1]
    
    # 1. Downtrend Check (Market was coming down)
    prior_candles = df.iloc[-5:-2]
    is_downtrend = prior_candles['close'].iloc[-1] < prior_candles['open'].iloc[0]

    # 2. Candle 1 Conditions (GREEN, touches SNR Support, closes ABOVE SNR)
    is_candle_1_green = candle_1['close'] > candle_1['open']
    touches_snr_1 = candle_1['low'] <= snr_support_level
    closes_above_snr_1 = candle_1['close'] > snr_support_level

    # 3. Candle 2 Conditions (RED, breaks SNR Support and closes BELOW SNR)
    is_candle_2_red = candle_2['close'] < candle_2['open']
    breaks_snr_2 = candle_2['close'] < snr_support_level

    # Final Signal Decision
    if is_downtrend and is_candle_1_green and touches_snr_1 and closes_above_snr_1 and is_candle_2_red and breaks_snr_2:
        return "PUT"  # Next candle DOWN signal

    return None
  
