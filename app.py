import streamlit as st
import requests

WEBHOOK_URL_WMG = st.secrets['url_lst']['webhook_wmg']
logo_path = "imgs/wmg_logo.png"

# st.write(f"Webhook URL is: {WEBHOOK_URL_WMG}")
left, mid, right = st.columns([1, 6, 1])

with mid:
    st.title("Wesnoth Modders Guild")
    st.subheader("Communication Messaging App on Streamlit")

with left:
    st.image(logo_path)