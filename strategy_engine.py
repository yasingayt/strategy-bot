from image_reader import analyze_candles

def analyze_chart(image_file, symbol):
    data = analyze_candles(image_file)

    trend = data['trend']
    candle_type = data['candle']
    if trend == "صاعد" and candle_type == "شمعة ابتلاعية صاعدة":
        signal = "شراء"
        entry = data['high']
        tp = round(entry + (entry * 0.002), 4)
        sl = round(entry - (entry * 0.0015), 4)
        reason = "شمعة ابتلاعية صاعدة بعد اتجاه صاعد واضح"
    elif trend == "هابط" and candle_type == "شمعة ابتلاعية هابطة":
        signal = "بيع"
        entry = data['low']
        tp = round(entry - (entry * 0.002), 4)
        sl = round(entry + (entry * 0.0015), 4)
        reason = "شمعة ابتلاعية هابطة بعد اتجاه هابط واضح"
    else:
        signal = "لا توجد صفقة"
        entry = tp = sl = "-"
        reason = "لم يتم التعرف على فرصة قوية واضحة"

    return {
        "trend": trend,
        "candle": candle_type,
        "signal": signal,
        "entry": entry,
        "tp": tp,
        "sl": sl,
        "reason": reason
    }
