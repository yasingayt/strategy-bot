from typing import List
from PIL import Image
import re

def extract_symbol_timeframe(filename: str):
    """
    يستخرج الزوج والفريم الزمني من اسم الملف (مثل GBPUSD_15M.jpg)
    """
    filename = filename.lower()
    match = re.match(r"([a-z]{6})[_\-]?(\d{1,2}[mh])", filename)
    if match:
        symbol = match.group(1).upper()
        tf = match.group(2).upper()
        return symbol, tf
    return "زوج غير معروف", "فريم غير معروف"

def detect_trend(prices: List[float]) -> str:
    """
    تحليل الاتجاه بناءً على تسلسل أسعار الإغلاق
    """
    if len(prices) < 3:
        return "غير معروف"
    
    ups = sum(prices[i] < prices[i+1] for i in range(len(prices)-1))
    downs = sum(prices[i] > prices[i+1] for i in range(len(prices)-1))

    if ups >= len(prices) * 0.7:
        return "صاعد"
    elif downs >= len(prices) * 0.7:
        return "هابط"
    else:
        return "عرضي"

def detect_candle_type(open_price, close_price, high_price, low_price) -> str:
    """
    تحديد نوع الشمعة الأخيرة (ابتلاعية، دوجي، قوية...)
    """
    body = abs(close_price - open_price)
    range_ = high_price - low_price
    if range_ == 0:
        return "شمعة غير صالحة"

    body_ratio = body / range_

    if body_ratio > 0.7:
        if close_price > open_price:
            return "شمعة صاعدة قوية"
        else:
            return "شمعة هابطة قوية"
    elif body_ratio < 0.2:
        return "شمعة دوجي"
    else:
        if close_price > open_price:
            return "شمعة صاعدة"
        else:
            return "شمعة هابطة"
