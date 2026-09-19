import pandas as pd

def check_strategy_4(df):
    """
    Setup - 4: Bullish Exhaustion Candle Reversal (DOWN Signal)
    
    Conditions:
    1. 4 consecutive GREEN candles (candle 1, 2, 3, 4).
    2. Total body size of candle 1 + candle 2 + candle 3 <= candle 4 size.
    """
    if len(df) < 4:
        return None

    # Getting last 4 candles
    c1 = df.iloc[-4]  # 1-no Green Candle
    c2 = df.iloc[-3]  # 2-no Green Candle
    c3 = df.iloc[-2]  # 3-no Green Candle
    c4 = df.iloc[-1]  # 4-no Exhaustion Green Candle

    # 1. Color Check: All 4 candles must be GREEN
    is_c1_green = c1['close'] > c1['open']
    is_c2_green = c2['close'] > c2['open']
    is_c3_green = c3['close'] > c3['open']
    is_c4_green = c4['close'] > c4['open']

    all_four_green = is_c1_green and is_c2_green and is_c3_green and is_c4_green

    # 2. Size Calculation (Body size = abs(close - open))
    size_1 = abs(c1['close'] - c1['open'])
    size_2 = abs(c2['close'] - c2['open'])
    size_3 = abs(c3['close'] - c3['open'])
    size_4 = abs(c4['close'] - c4['open'])

    total_first_three_size = size_1 + size_2 + size_3

    # 3. Size Comparison: (1 + 2 + 3 <= 4)
    # Allowing a 5% margin for approximate matching
    is_size_matched = size_4 >= (total_first_three_size * 0.95)

    # Final Decision
    if all_four_green and is_size_matched:
        return "PUT"  # Next candle DOWN signal

    return None
  
