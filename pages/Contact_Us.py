import streamlit as st
from send_email import send_email

st.title("Contact Us")

with st.form(key="forum"):
    email = st.text_input("Your email adress")
    raw_mesaj = st.text_area("Your message")
    mesaj = f"""\
Subject: New email from {email}

{raw_mesaj}
From: {email}
"""
    buton = st.form_submit_button("Submit")
    if buton:
        send_email(mesaj)
        st.info("Your email was sent succesfully!")