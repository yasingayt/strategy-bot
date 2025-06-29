from utils import extract_symbol_timeframe, detect_trend, detect_candle_type

def analyze_chart(uploaded_file):
    import cv2
    import numpy as np
    from PIL import Image
    import io

    # تحميل الصورة وتحويلها إلى بيانات NumPy
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    # تحليل بيانات الصورة بشكل مبسط (نموذج تجريبي)
    # 🚩 ملاحظة: هنا تُفترض بيانات سعرية وهمية للتحليل التجريبي
    close_prices = [1.1000, 1.1012, 1.1035, 1.1048, 1.1060, 1.1085, 1.1100]
    last_open = 1.1060
    last_close = 1.1100
    last_high = 1.1110
    last_low = 1.1055

    # تحليل الاتجاه العام
    trend = detect_trend(close_prices)

    # تحليل نوع آخر شمعة
    candle_type = detect_candle_type(last_open, last_close, last_high, last_low)

    # منطق التوصية
    recommendation = "لا توجد صفقة"
    entry_point = "-"
    tp = "-"
    sl = "-"
    reason = ""

    if trend == "صاعد" and candle_type == "شمعة قوية":
        recommendation = "شراء"
        entry_point = last_close
        tp = round(last_close + 0.0020, 5)
        sl = round(last_close - 0.0010, 5)
        reason = "الاتجاه صاعد وظهرت شمعة صعود قوية"

    elif trend == "هابط" and candle_type == "شمعة قوية":
        recommendation = "بيع"
        entry_point = last_close
        tp = round(last_close - 0.0020, 5)
        sl = round(last_close + 0.0010, 5)
        reason = "الاتجاه هابط وظهرت شمعة هبوط قوية"

    else:
        reason = "لم يتم التعرف على فرصة قوية وواضحة"

    # استخراج اسم الزوج والفريم من اسم الصورة
    symbol, timeframe = extract_symbol_timeframe(uploaded_file.name)

    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "trend": trend,
        "candle_type": candle_type,
        "recommendation": recommendation,
        "entry": entry_point,
        "tp": tp,
        "sl": sl,
        "reason": reason
    }
