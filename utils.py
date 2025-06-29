def extract_symbol_timeframe(filename):
    """
    استخراج اسم الزوج والفريم من اسم الملف مثل: GBPUSD_15m أو EURUSD_H1
    """
    filename = filename.lower()
    for tf in ["1m", "5m", "15m", "30m", "1h", "4h", "1d"]:
        if tf in filename:
            symbol = filename.replace(tf, "").replace("_", "").replace(".png", "").replace(".jpg", "").replace(".jpeg", "")
            return symbol.upper(), tf
    return "زوج غير معروف", "فريم غير معروف"

def detect_trend(candles):
    """
    تحديد الاتجاه العام اعتمادًا على مقارنة عدد الشموع الصاعدة بالهابطة
    """
    ups = sum(1 for c in candles if c["close"] > c["open"])
    downs = sum(1 for c in candles if c["close"] < c["open"])

    if ups > downs:
        return "صاعد"
    elif downs > ups:
        return "هابط"
    else:
        return "الاتجاه غير واضح"

def detect_candle_type(open_price, close_price, high_price, low_price):
    """
    تحديد نوع الشمعة الأخيرة (صاعدة قوية، هابطة قوية، دوجي، عادية...)
    """
    body = abs(close_price - open_price)
    range_ = high_price - low_price
    if range_ == 0:
        return "شمعة غير صالحة"

    body_ratio = body / range_

    if body_ratio >= 0.7:
        if close_price > open_price:
            return "شمعة صاعدة قوية"
        elif open_price > close_price:
            return "شمعة هابطة قوية"
    elif body_ratio < 0.2:
        return "شمعة دوجي"
    else:
        if close_price > open_price:
            return "شمعة صاعدة ضعيفة"
        else:
            return "شمعة هابطة ضعيفة"
