import streamlit as st
from strategy_engine import analyze_chart
from utils import extract_pair_name
from PIL import Image

st.set_page_config(page_title="📊 تحليل تلقائي من صورة الشارت", layout="wide")
st.title("📸 ارفع صورة الشارت - واحصل على توصية ذكية")

uploaded_file = st.file_uploader("ارفع صورة الشارت (PNG / JPG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="📈 الصورة المرفوعة", use_column_width=True)

    with st.spinner("جاري تحليل الصورة..."):
        symbol = extract_pair_name(uploaded_file)
        result = analyze_chart(uploaded_file, symbol)

    st.success("✅ التوصية الذكية جاهزة:")
    st.markdown(f'''
    ### 🔎 الزوج: **{symbol}**
    - 📈 الاتجاه: **{result['trend']}**
    - 💥 نوع الشمعة: **{result['candle']}**
    - 🎯 الصفقة: **{result['signal']}**
    - 📍 نقطة الدخول: `{result['entry']}`
    - 🎯 الهدف: `{result['tp']}`
    - ⛔ وقف الخسارة: `{result['sl']}`
    - 🧠 سبب الدخول: {result['reason']}
    ''')
