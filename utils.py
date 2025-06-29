import re
import numpy as np

# استخراج اسم الزوج والفريم من اسم الصورة
def extract_symbol_timeframe(filename):
    filename = filename.lower()
    match = re.search(r"([a-z]{6,7})(\d{1,2}m|[1-4]h|1d)", filename)
    if match:
        symbol = match.group(1).upper()
        timeframe = match.group(2).upper()
        return symbol, timeframe
    return "زوج غير معروف", "فريم غير معروف"

# تحليل الاتجاه العام من قائمة أسعار (قيمة الإغلاق)
def detect_trend(close_prices):
    if len(close_prices) < 5:
        return "اتجاه غير كافٍ"

    trend_score = np.polyfit(range(len(close_prices)), close_prices, 1)[0]

    if trend_score > 0.01:
        return "صاعد"
    elif trend_score < -0.01:
        return "هابط"
    else:
        return "عرضي"

# تحديد نوع الشمعة (ابتلاعية، قوية، ضعيفة...)
def detect_candle_type(open_price, close_price, high_price, low_price):
    body = abs(close_price - open_price)
    total_range = high_price - low_price
    if total_range == 0:
        return "شمعة غير صالحة"

    body_ratio = body / total_range

    if body_ratio > 0.7:
        return "شمعة قوية"
    elif body_ratio > 0.4:
        return "شمعة عادية"
    else:
        return "شمعة ضعيفة"
