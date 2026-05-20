import streamlit as st

st.title("GPP Calculator")

# Input
lbs = st.number_input("LBS", value=0.0)
gpp = st.number_input("GPP", value=0.0)

# Arrow
arrow = lbs * gpp * 0.0647989

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

st.write("Arrow:", round(arrow, 2))
st.write("Spine:", spine)
