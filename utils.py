import re
import numpy as np

def extract_symbol_timeframe(file) -> tuple:
    filename = file.name.lower()
    symbol_match = re.search(r"(xauusd|eurusd|gbpusd|usdjpy|usdchf|usdcad|audusd|nzdusd)", filename)
    tf_match = re.search(r"(m1|m5|m15|m30|h1|h4|d1|w1)", filename)

    symbol = symbol_match.group(1).upper() if symbol_match else "زوج غير معروف"
    timeframe = tf_match.group(1).upper() if tf_match else "فريم غير معروف"
    return symbol, timeframe

def detect_trend(close_prices):
    if len(close_prices) < 3:
        return "بيانات غير كافية"
    slope = np.polyfit(range(len(close_prices)), close_prices, 1)[0]
    if slope > 0.0005:
        return "صاعد"
    elif slope < -0.0005:
        return "هابط"
    else:
        return "عرضي"

def detect_candle_type(open_price, close_price, high_price, low_price):
    body = abs(close_price - open_price)
    total_range = high_price - low_price
    if total_range == 0:
        return "شمعة غير صالحة"

    ratio = body / total_range
    if ratio > 0.7:
        return "شمعة قوية"
    elif ratio > 0.4:
        return "شمعة متوسطة"
    else:
        return "شمعة ضعيفة"
