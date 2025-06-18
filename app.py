import streamlit as st
import pandas as pd
from generate_token import generate_token
from verify_token import verify_token, public_key
from vendor_risk import compute_risk_scores

st.title("Quantum Supply Chain MVP - Unified Dashboard")

tab1, tab2 = st.tabs(["Token Authentication", "Vendor Reliability Scoring"])

with tab1:
    st.header("Visual Token Authentication")

    shipment_id = st.text_input("Shipment ID", "SHIP12345")
    origin = st.text_input("Origin", "Durham Distribution")

    if st.button("Generate Token"):
        token = generate_token(shipment_id, origin)
        st.image("token.png")
        st.success("Token generated and signed!")

        st.subheader("🔐 Token JSON")
        st.json(token)

        import io
        import json
        json_bytes = io.BytesIO(json.dumps(token).encode("utf-8"))
        st.download_button(
            label="⬇️ Download Token JSON",
            data=json_bytes,
            file_name="token.json",
            mime="application/json"
        )

    uploaded = st.file_uploader("Upload token JSON for verification", type="json")
    if uploaded:
        import json
        token_data = json.load(uploaded)
        if verify_token(token_data, public_key):
            st.success("✅ Token is authentic!")
        else:
            st.error("🚫 Invalid or tampered token!")

with tab2:
    st.header("Vendor Reliability Scoring")

    uploaded_file = st.file_uploader("Upload vendor CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file, sep=r'\s+', engine='python')
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        df.columns = df.columns.str.strip()

        st.write("Columns detected in CSV:", df.columns.tolist())

        scored = compute_risk_scores(df)

        st.write("## Vendor Risk Scores")
        st.dataframe(scored.style.background_gradient(subset=['risk_score'], cmap='RdYlGn_r'))

        high_risk = scored[scored['risk_score'] > 0.6]
        if not high_risk.empty:
            st.warning(f"⚠️ High risk vendors detected:\n{', '.join(high_risk['vendor_name'])}")


