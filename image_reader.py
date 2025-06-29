import re

def extract_symbol_timeframe(file) -> tuple:
    # محاولة قراءة اسم الملف، أو وضع اسم افتراضي عند عدم توفره
    try:
        filename = file.name.lower()
    except AttributeError:
        filename = "unknown_gbpusd_m15.png"  # اسم افتراضي لتفادي الخطأ

    # استخراج رمز الزوج والفريم من الاسم
    symbol_match = re.search(r"(xauusd|eurusd|gbpusd|usdjpy|usdchf|usdcad|audusd|nzdusd)", filename)
    tf_match = re.search(r"(m1|m5|m15|m30|h1|h4|d1|w1)", filename)

    symbol = symbol_match.group(1).upper() if symbol_match else "زوج غير معروف"
    timeframe = tf_match.group(1).upper() if tf_match else "فريم غير معروف"
    return symbol, timeframe


def detect_trend(candles) -> str:
    # دالة بسيطة لتحديد الاتجاه حسب آخر الشموع
    ups = 0
    downs = 0
    for i in range(1, len(candles)):
        if candles[i]["close"] > candles[i]["open"]:
            ups += 1
        elif candles[i]["close"] < candles[i]["open"]:
            downs += 1
    if ups > downs:
        return "صاعد"
    elif downs > ups:
        return "هابط"
    else:
        return "عرضي"


def detect_candle_type(candle: dict) -> str:
    # تحديد نوع الشمعة الواحدة حسب الجسم والذيل
    body = abs(candle["close"] - candle["open"])
    wick = candle["high"] - candle["low"]
    if body > wick * 0.6:
        return "شمعة قوية"
    elif body < wick * 0.3:
        return "شمعة ضعيفة"
    else:
        return "شمعة عادية"
