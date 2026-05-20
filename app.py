import streamlit as st

st.set_page_config(page_title="GPP Calculator", layout="centered")

# CSS custom
st.markdown("""
<style>
.big-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
}
.result-box {
    font-size: 34px;
    font-weight: bold;
    padding: 15px;
    border-radius: 10px;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">GPP Calculator</p>', unsafe_allow_html=True)

# Input
lbs = st.number_input("LBS", min_value=0, step=1)
gpp = st.number_input("GPP", min_value=0, step=1)

# Arrow (tanpa desimal)
arrow = round(lbs * gpp * 0.0647989)

# Spine logic
spine = ""

if 30 <= lbs <= 35:
    spine = 600
elif 36 <= lbs <= 39:
    spine = 550
elif 40 <= lbs <= 45:
    spine = 500
elif 46 <= lbs <= 49:
    spine = 450
elif 50 <= lbs <= 55:
    spine = 400
elif 56 <= lbs <= 59:
    spine = 350
elif 60 <= lbs <= 65:
    spine = 300
elif 66 <= lbs <= 69:
    spine = 250
elif 70 <= lbs <= 100:
    spine = 200

# Output besar
st.markdown(f'<div class="result-box">Arrow: {arrow}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="result-box">Spine: {spine}</div>', unsafe_allow_html=True)
