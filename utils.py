from typing import List, Tuple
import re
from PIL import Image
import pytesseract

# ✅ استخراج اسم الزوج والفريم من اسم الملف
def extract_symbol_timeframe(filename: str) -> Tuple[str, str]:
    filename = filename.name.lower() if hasattr(filename, 'name') else filename.lower()
    match = re.search(r"(gbpusd|eurusd|xauusd).*?(1m|5m|15m|30m|1h|4h|1d)", filename)
    if match:
        return match.group(1).upper(), match.group(2).upper()
    return "زوج غير معروف", "فريم غير معروف"

# ✅ كشف نوع الشمعة الأخيرة
def detect_candle_type(close_prices: List[float]) -> str:
    if len(close_prices) < 3:
        return "غير كافية"
    body = abs(close_prices[-1] - close_prices[-2])
    previous_body = abs(close_prices[-2] - close_prices[-3])
    if body > previous_body * 1.3:
        return "شمعة قوية"
    elif body < previous_body * 0.5:
        return "شمعة ضعيفة"
    else:
        return "شمعة عادية"

# ✅ كشف الاتجاه العام
def detect_trend(candles) -> str:
    try:
        # إذا كان كل عنصر dict يحتوي على open/close
        if isinstance(candles[0], dict):
            ups = sum(1 for c in candles if c["close"] > c["open"])
            downs = sum(1 for c in candles if c["close"] < c["open"])
        else:
            # إذا كانت قائمة أسعار فقط
            ups = sum(1 for i in range(1, len(candles)) if candles[i] > candles[i-1])
            downs = sum(1 for i in range(1, len(candles)) if candles[i] < candles[i-1])
    except Exception as e:
        print("Trend Detection Error:", e)
        return "غير معروف"

    if ups > downs:
        return "صاعد"
    elif downs > ups:
        return "هابط"
    else:
        return "عرضي"

# ✅ تحويل صورة إلى نص باستخدام OCR
def extract_text_from_image(image_path: str) -> str:
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='eng+ara')
        return text
    except Exception as e:
        return f"خطأ في قراءة الصورة: {str(e)}"
