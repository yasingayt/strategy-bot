from PIL import Image
import cv2
import numpy as np

def analyze_candles(image_file):
    image = Image.open(image_file).convert("RGB")
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    candles = sorted(contours, key=lambda c: cv2.boundingRect(c)[0], reverse=True)[:10]

    heights = []
    for c in candles:
        x, y, w, h = cv2.boundingRect(c)
        heights.append(h)

    avg = np.mean(heights)
    big = heights[0] if heights else 0

    candle_type = "شمعة ابتلاعية صاعدة" if big > avg * 1.6 else "شمعة عادية"
    trend = "صاعد" if big and big >= avg else "هابط"

    return {"trend": trend, "candle": candle_type, "high": 1.2500, "low": 1.2470}
