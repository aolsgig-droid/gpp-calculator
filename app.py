import streamlit as st

st.set_page_config(page_title="GPP Calculator", layout="centered")

# Custom CSS
st.markdown("""
<style>
.big-title {
    font-size: 44px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 30px;
}

label {
    font-size: 28px !important;
    font-weight: bold !important;
}

div[data-baseweb="input"] input {
    font-size: 30px !important;
    height: 60px !important;
    text-align: center;
    font-weight: bold;
}

.result-box {
    font-size: 36px;
    font-weight: bold;
    text-align: center;
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
    background-color: #f4f4f4;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<p class="big-title">GPP CALCULATOR</p>',
    unsafe_allow_html=True
)

# Input pakai 2 kolom
col1, col2 = st.columns(2)

with col1:
    lbs = st.number_input("LBS", min_value=0, step=1)

with col2:
    gpp = st.number_input("GPP", min_value=0, step=1)

# Arrow calculation
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

# Output Arrow
st.markdown(
    f'<div class="result-box">Arrow: {arrow:,} gram</div>',
    unsafe_allow_html=True
)

# Output Spine
st.markdown(
    f'<div class="result-box">Spine: {spine}</div>',
    unsafe_allow_html=True
)
