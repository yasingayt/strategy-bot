from PIL import Image
import pytesseract

def extract_pair_name(image_file):
    try:
        img = Image.open(image_file)
        text = pytesseract.image_to_string(img).upper()
        if "XAUUSD" in text:
            return "XAUUSD"
        elif "EURUSD" in text:
            return "EURUSD"
        elif "GBPUSD" in text:
            return "GBPUSD"
        else:
            return "زوج غير معروف"
    except:
        return "زوج غير معروف"
