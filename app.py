import streamlit as st
from generate_token import generate_token
from verify_token import verify_token, public_key

st.title("🔐 Visual Token Authentication Demo")

shipment_id = st.text_input("Shipment ID", "SHIP12345")
origin = st.text_input("Origin", "Durham Distribution")

if st.button("Generate Token"):
    token = generate_token(shipment_id, origin)
    st.image("token.png")
    st.success("Token generated and signed!")

uploaded = st.file_uploader("Upload token JSON for verification", type="json")

if uploaded:
    import json
    token_data = json.load(uploaded)
    if verify_token(token_data, public_key):
        st.success("✅ Token is authentic!")
    else:
        st.error("🚫 Invalid or tampered token!")
