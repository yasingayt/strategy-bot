import streamlit as st
from strategy_engine import analyze_chart
from utils import extract_symbol_timeframe
from PIL import Image

st.set_page_config(page_title="بوت تحليل شارت 🔍", layout="wide")
st.title("📈 بوت التوصية الذكي - تحليل صورة شارت")

uploaded_file = st.file_uploader("🖼️ ارفع صورة الشارت (PNG / JPG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 صورة الشارت المرفوعة", use_column_width=True)

    with st.spinner("⏳ يجري تحليل الصورة..."):
        result = analyze_chart(uploaded_file)

    st.success("✅ التوصية الذكية جاهزة:")

    st.markdown(f"""
    ### 🔍 الزوج: {result['symbol']} - {result['timeframe']}
    - 🔁 الاتجاه: **{result['trend']}**
    - 🕯️ نوع الشمعة: **{result['candle_type']}**
    - 🎯 التوصية: **{result['recommendation']}**
    - 📍 نقطة الدخول: `{result['entry']}`
    - 🎯 الهدف: `{result['tp']}`
    - 🛑 وقف الخسارة: `{result['sl']}`
    - 💬 السبب: _{result['reason']}_
    """)
else:
    st.info("👆 قم برفع صورة شارت ليتم تحليلها.")
