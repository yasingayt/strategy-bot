import re

def extract_symbol_timeframe(filename):
    """
    استخراج اسم الزوج والفريم الزمني من اسم الملف.
    مثال: GBPUSD_15m.jpg → (GBPUSD, 15m)
    """
    filename = filename.lower()
    match = re.search(r"([a-z]{6,7})[_\- ]?(\d{1,2}[mh])", filename)
    if match:
        return match.group(1).upper(), match.group(2)
    return "زوج غير معروف", "فريم غير معروف"

def detect_trend(candles):
    """
    تحليل الاتجاه العام بناءً على إغلاق وفتح الشموع.
    """
    ups = sum(1 for c in candles if c["close"] > c["open"])
    downs = sum(1 for c in candles if c["close"] < c["open"])

    if ups > downs:
        return "صاعد"
    elif downs > ups:
        return "هابط"
    else:
        return "الاتجاه غير واضح"

def detect_candle_type(open_price, close_price, high, low):
    """
    تصنيف نوع الشمعة (قوية أو ضعيفة).
    """
    body = abs(close_price - open_price)
    total = high - low
    if total == 0:
        return "شمعة غير صالحة"
    body_ratio = body / total

    if body_ratio > 0.6:
        if close_price > open_price:
            return "شمعة صاعدة قوية"
        elif open_price > close_price:
            return "شمعة هابطة قوية"
    else:
        return "شمعة ضعيفة"

def is_bullish_engulfing(prev_candle, curr_candle):
    return (
        prev_candle["close"] < prev_candle["open"] and
        curr_candle["close"] > curr_candle["open"] and
        curr_candle["open"] < prev_candle["close"] and
        curr_candle["close"] > prev_candle["open"]
    )

def is_bearish_engulfing(prev_candle, curr_candle):
    return (
        prev_candle["close"] > prev_candle["open"] and
        curr_candle["close"] < curr_candle["open"] and
        curr_candle["open"] > prev_candle["close"] and
        curr_candle["close"] < prev_candle["open"]
    )
