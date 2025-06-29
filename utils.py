import re

def extract_symbol_timeframe(file) -> tuple:
    # محاولة آمنة للحصول على اسم الملف
    filename = getattr(file, "name", "").lower()
    if not filename:
        filename = "unknown_gbpusd_m15.png"  # اسم افتراضي عند عدم وجود اسم ملف

    # استخراج رمز الزوج والفريم من الاسم
    symbol_match = re.search(r"(xauusd|eurusd|gbpusd|usdjpy|usdchf|usdcad|audusd|nzdusd)", filename)
    tf_match = re.search(r"(m1|m5|m15|m30|h1|h4|d1|w1)", filename)

    symbol = symbol_match.group(1).upper() if symbol_match else "زوج غير معروف"
    timeframe = tf_match.group(1).upper() if tf_match else "فريم غير معروف"
    return symbol, timeframe


def detect_trend(candles) -> str:
    ups = sum(1 for c in candles if c["close"] > c["open"])
    downs = sum(1 for c in candles if c["close"] < c["open"])
    if ups > downs:
        return "صاعد"
    elif downs > ups:
        return "هابط"
    else:
        return "عرضي"


def detect_candle_type(candle: dict) -> str:
    body = abs(candle["close"] - candle["open"])
    wick = candle["high"] - candle["low"]
    if body > wick * 0.6:
        return "شمعة قوية"
    elif body < wick * 0.3:
        return "شمعة ضعيفة"
    else:
        return "شمعة عادية"
