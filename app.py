# Inside your Streamlit app at the top of app.py
import streamlit as st

st.set_page_config(page_title="AI Document Assistant", layout="wide")

# Allow iframe embedding explicitly
st.markdown(
    "<style>iframe {width:100%; height:100%;}</style>",
    unsafe_allow_html=True
)
