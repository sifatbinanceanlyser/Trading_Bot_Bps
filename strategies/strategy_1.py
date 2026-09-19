import pandas as pd

def check_strategy_1(df, snr_resistance_level):
    """
    Setup - 1: SNR Breakout Setup (UP Signal)
    """
    if len(df) < 5:
        return None

    candle_1 = df.iloc[-2]  # 1-no Red Candle
    candle_2 = df.iloc[-1]  # 2-no Green Candle

    # Point 1: Market oporer dike jabe (Uptrend check)
    prior_candles = df.iloc[-5:-2]
    is_uptrend = prior_candles['close'].iloc[-1] > prior_candles['open'].iloc[0]

    # Point 2: 1-no candle RED hobe, Resistance touch korbe, niche close hobe
    is_candle_1_red = candle_1['close'] < candle_1['open']
    touches_snr_1 = candle_1['high'] >= snr_resistance_level
    closes_below_snr_1 = candle_1['close'] < snr_resistance_level

    # Point 3: 2-no candle GREEN hobe, Resistance break kore opore close hobe
    is_candle_2_green = candle_2['close'] > candle_2['open']
    breaks_snr_2 = candle_2['close'] > snr_resistance_level

    # Sob condition match korle Porer candle UP (CALL)
    if is_uptrend and is_candle_1_red and touches_snr_1 and closes_below_snr_1 and is_candle_2_green and breaks_snr_2:
        return "CALL"  # UP Signal

    return None
  
