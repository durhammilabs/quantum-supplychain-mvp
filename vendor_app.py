import streamlit as st
import pandas as pd
from vendor_risk import compute_risk_scores

st.title("Vendor Reliability Scoring")

uploaded_file = st.file_uploader("Upload vendor CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file, sep=r'\s+', engine='python')
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df.columns = df.columns.str.strip()

    st.write("Columns detected in CSV:", df.columns.tolist())  # Debug print

    scored = compute_risk_scores(df)

    st.write("## Vendor Risk Scores")
    st.dataframe(scored.style.background_gradient(subset=['risk_score'], cmap='RdYlGn_r'))

    high_risk = scored[scored['risk_score'] > 0.6]
    if not high_risk.empty:
        st.warning(f"⚠️ High risk vendors detected:\n{', '.join(high_risk['vendor_name'])}")
