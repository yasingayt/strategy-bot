from PIL import Image
import numpy as np

def detect_trend(image):
    """
    تحليل بدائي للاتجاه بناءً على توزيع الألوان العمودية.
    سيتم تحسينه لاحقًا باستخدام تحليل أكثر دقة للقمم والقيعان.
    """
    image = image.convert("L")
    arr = np.array(image)

    top = np.mean(arr[:int(arr.shape[0] / 2), :])
    bottom = np.mean(arr[int(arr.shape[0] / 2):, :])

    if bottom < top - 10:
        return "صاعد"
    elif top < bottom - 10:
        return "هابط"
    else:
        return "عرضي"

def detect_candle_strength(image):
    """
    تحليل بدائي لحجم الشمعة الأخيرة بناءً على الطول الرأسي للعنصر الأيمن في الصورة.
    """
    gray = image.convert("L")
    arr = np.array(gray)

    right_half = arr[:, int(arr.shape[1]*0.7):]  # آخر جزء من الشارت
    vertical_std = np.std(right_half, axis=1)
    diff = np.max(vertical_std) - np.min(vertical_std)

    if diff > 15:
        return "ابتلاع صاعد"
    elif diff < -15:
        return "ابتلاع هابط"
    else:
        return "شمعة ضعيفة"
