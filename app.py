import streamlit as st
import pandas as pd
from generate_token import generate_token
from verify_token import verify_token, public_key
from vendor_risk import compute_risk_scores

st.title("Quantum Supply Chain MVP - Unified Dashboard")

tab1, tab2 = st.tabs(["Token Authentication", "Vendor Reliability Scoring"])

with tab1:
    st.header("Visual Token Authentication")
    st.write(
        "Generate cryptographically signed shipment tokens and verify authenticity "
        "using QR codes and JSON uploads."
    )
    shipment_id = st.text_input(
        "Shipment ID",
        "SHIP12345",
        help="Enter a unique shipment identifier (e.g., order number)."
    )
    origin = st.text_input(
        "Origin",
        "Durham Distribution",
        help="Enter the origin location or warehouse."
    )

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

    uploaded = st.file_uploader(
        "Upload token JSON for verification",
        type="json",
        help="Upload a previously generated token JSON file to verify authenticity."
    )
    if uploaded:
        try:
            import json
            token_data = json.load(uploaded)
            if verify_token(token_data, public_key):
                st.success("✅ Token is authentic!")
            else:
                st.error("🚫 Invalid or tampered token!")
        except Exception as e:
            st.error(f"Error reading token file: {e}")

with tab2:
    st.header("Vendor Reliability Scoring")
    st.write(
        "Upload a CSV file containing vendor performance data to compute risk scores "
        "and identify high-risk vendors."
    )

    uploaded_file = st.file_uploader(
        "Upload vendor CSV",
        type="csv",
        help=(
            "CSV must include columns: vendor_id, vendor_name, on_time_pct, "
            "claim_rate, geopolitical_risk, past_delays."
        )
    )
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file, sep=r'\s+', engine='python')
            df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
            df.columns = df.columns.str.strip()

            required_cols = [
                'vendor_id', 'vendor_name', 'on_time_pct',
                'claim_rate', 'geopolitical_risk', 'past_delays'
            ]
            missing_cols = [c for c in required_cols if c not in df.columns]
            if missing_cols:
                st.error(f"Missing required columns: {', '.join(missing_cols)}")
            else:
                st.write("Columns detected in CSV:", df.columns.tolist())

                scored = compute_risk_scores(df)

                st.write("## Vendor Risk Scores")
                st.dataframe(scored.style.background_gradient(subset=['risk_score'], cmap='RdYlGn_r'))

                high_risk = scored[scored['risk_score'] > 0.6]
                if not high_risk.empty:
                    st.warning(f"⚠️ High risk vendors detected:\n{', '.join(high_risk['vendor_name'])}")

        except Exception as e:
            st.error(f"Error processing CSV file: {e}")

    st.markdown("<br>", unsafe_allow_html=True)
