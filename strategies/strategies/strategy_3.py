import pandas as pd

def check_strategy_3(df):
    """
    Setup - 3: Exhaustion Candle Reversal (UP Signal)
    
    Conditions:
    1. 4 consecutive RED candles (candle 1, 2, 3, 4).
    2. Total size of candle 1 + candle 2 + candle 3 <= candle 4 size.
    """
    if len(df) < 4:
        return None

    # Getting last 4 candles
    c1 = df.iloc[-4]  # 1-no Red Candle
    c2 = df.iloc[-3]  # 2-no Red Candle
    c3 = df.iloc[-2]  # 3-no Red Candle
    c4 = df.iloc[-1]  # 4-no Exhaustion Red Candle

    # 1. Color Check: All 4 candles must be RED
    is_c1_red = c1['close'] < c1['open']
    is_c2_red = c2['close'] < c2['open']
    is_c3_red = c3['close'] < c3['open']
    is_c4_red = c4['close'] < c4['open']

    all_four_red = is_c1_red and is_c2_red and is_c3_red and is_c4_red

    # 2. Size Calculation (Total vertical length from High to Low or Open to Close)
    # Using total body size (abs(open - close)) as per trading candle logic
    size_1 = abs(c1['open'] - c1['close'])
    size_2 = abs(c2['open'] - c2['close'])
    size_3 = abs(c3['open'] - c3['close'])
    size_4 = abs(c4['open'] - c4['close'])

    total_first_three_size = size_1 + size_2 + size_3

    # 3. Size Comparison: (1 + 2 + 3 <= 4)
    # Allowing a 5% margin for exact/approximate matching
    is_size_matched = size_4 >= (total_first_three_size * 0.95)

    # Final Decision
    if all_four_red and is_size_matched:
        return "CALL"  # Next candle UP signal

    return None
  
