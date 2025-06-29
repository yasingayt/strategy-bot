from utils import extract_symbol_timeframe, detect_trend, detect_candle_type
import random

def analyze_chart(image):
    try:
        # استخراج اسم الزوج والفريم من اسم الصورة
        symbol, timeframe = extract_symbol_timeframe(image)

        # تحليل الاتجاه من الصورة
        trend = detect_trend(image)

        # تحليل نوع الشمعة الأخيرة
        candle = detect_candle_type(image)

        # توليد توصية على أساس الاتجاه + الشمعة
        if trend == "صاعد" and candle == "شمعة ابتلاعية صاعدة":
            signal = "شراء"
            entry = "عند كسر قمة الشمعة"
            tp = "أعلى 3 شموع سابقة"
            sl = "أسفل الشمعة السابقة"
        elif trend == "هابط" and candle == "شمعة ابتلاعية هابطة":
            signal = "بيع"
            entry = "عند كسر قاع الشمعة"
            tp = "أدنى 3 شموع سابقة"
            sl = "أعلى الشمعة السابقة"
        else:
            signal = "لا توجد صفقة قوية حالياً"
            entry = tp = sl = "-"

        return {
            "status": "ok",
            "symbol": symbol,
            "timeframe": timeframe,
            "trend": trend,
            "candle": candle,
            "signal": signal,
            "entry": entry,
            "tp": tp,
            "sl": sl
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
