import streamlit as st
from PIL import Image
from strategy_engine import analyze_chart
import os

st.set_page_config(page_title="تحليل الشارت الذكي", layout="centered")

st.title("📊 بوت التحليل الذكي من الصور")
st.markdown("ارفع صورة لشارت وسأعطيك توصية احترافية بناءً على تحليلي اليدوي الذكي")

uploaded_file = st.file_uploader("📤 ارفع صورة الشارت (من TradingView مثلًا)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة المرفوعة", use_column_width=True)

    with st.spinner("جاري تحليل الصورة..."):
        result = analyze_chart(image)

    st.markdown("---")
    st.subheader("📌 نتيجة التحليل:")

    if result["status"] == "ok":
        st.markdown(f"### الزوج: `{result['symbol']}`")
        st.markdown(f"### الفريم: `{result['timeframe']}`")
        st.markdown(f"### الاتجاه: `{result['trend']}`")
        st.markdown(f"### نوع الشمعة: `{result['candle']}`")
        st.markdown(f"### التوصية: `{result['signal']}`")

        st.success(f"🎯 نقطة الدخول: `{result['entry']}`")
        st.info(f"🎯 الهدف (TP): `{result['tp']}`")
        st.error(f"🛑 الستوب (SL): `{result['sl']}`")
    else:
        st.warning("❌ لم يتمكن النظام من استخراج توصية دقيقة من هذه الصورة. جرب صورة أوضح.")
