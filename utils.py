import re
from typing import Tuple, List

# -------------------------------
# 1. استخراج اسم الزوج والزمن من اسم الصورة
# -------------------------------
def extract_symbol_timeframe(filename: str) -> Tuple[str, str]:
    """
    يحاول استخراج اسم الزوج والإطار الزمني من اسم الملف باستخدام regex.
    مثال على اسم الملف: 'GBPUSD_15m.jpg'
    """
    filename = filename.lower()
    match = re.search(r"([a-z]{6})[_\-]?(\d+[mh])", filename)
    if match:
        symbol = match.group(1).upper()
        timeframe = match.group(2).upper()
        return symbol, timeframe
    return "غير معروف", "غير معروف"

# -------------------------------
# 2. تحليل الاتجاه العام
# -------------------------------
def detect_trend(candles: List[dict]) -> str:
    """
    يحلل الاتجاه العام باستخدام نسبة الشموع الصاعدة والهابطة.
    الشمعة تُعد صاعدة إذا كان الإغلاق > الافتتاح.
    """
    ups = sum(1 for c in candles if c["close"] > c["open"])
    downs = sum(1 for c in candles if c["close"] < c["open"])
    total = len(candles)

    if total == 0:
        return "غير معروف"

    if ups >= total * 0.7:
        return "صاعد"
    elif downs >= total * 0.7:
        return "هابط"
    else:
        return "عرضي"

# -------------------------------
# 3. تحديد نوع الشمعة الأخيرة (قوية، ضعيفة، عادية)
# -------------------------------
def detect_candle_type(open_price: float, close_price: float, high_price: float, low_price: float) -> str:
    """
    يصنف الشمعة الأخيرة بناءً على حجم جسم الشمعة مقارنة بنطاقها الكلي.
    """
    body_size = abs(close_price - open_price)
    candle_range = high_price - low_price

    if candle_range == 0:
        return "شمعة غير صالحة"

    body_ratio = body_size / candle_range

    if body_ratio >= 0.7:
        return "شمعة قوية"
    elif body_ratio <= 0.2:
        return "شمعة ضعيفة"
    else:
        return "شمعة عادية"
