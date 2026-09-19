import pandas as pd

def check_strategy_5(df, snr_support_level):
    """
    Setup - 5: Support Doji Reversal Setup (UP Signal)
    
    Conditions:
    1. Downtrend: Market is coming down before Candle 1.
    2. Candle 1: Doji Candle (Open and Close are almost equal, very small body).
    3. Touches Support: Low <= SNR support level.
    4. Closes Above Support: Close > SNR support level.
    """
    if len(df) < 4:
        return None

    # Latest completed candle (1-no Doji candle in image)
    candle_1 = df.iloc[-1]

    # 1. Downtrend Check (Prior candles moving down)
    prior_candles = df.iloc[-4:-1]
    is_downtrend = prior_candles['close'].iloc[-1] < prior_candles['open'].iloc[0]

    # 2. Doji Candle Logic: Body size is very small relative to total range (High - Low)
    body_size = abs(candle_1['close'] - candle_1['open'])
    total_range = candle_1['high'] - candle_1['low']
    
    # Avoid zero division
    total_range = 0.00001 if total_range == 0 else total_range
    
    # Doji condition: Body is less than or equal to 10% of total candle range
    is_doji = (body_size / total_range) <= 0.10

    # 3. Touch SNR Support & Close ABOVE SNR
    touches_snr_1 = candle_1['low'] <= snr_support_level
    closes_above_snr_1 = candle_1['close'] > snr_support_level

    # Final Decision
    if is_downtrend and is_doji and touches_snr_1 and closes_above_snr_1:
        return "CALL"  # Next candle UP signal

    return None
      
