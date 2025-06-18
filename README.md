Quantum Supply Chain MVP

This project includes two key modules:

Visual Token Authentication: Secure QR-style tokens that verify shipment authenticity using cryptographic signatures.

Vendor Reliability Scoring: AI-driven system to score vendors based on shipment history and geopolitical risk.

How to Run

Token Authentication Module

Clone the repo:
git clone https://github.com/durhammilabs/quantum-supplychain-mvp.git
cd quantum-supplychain-mvp

Install dependencies:
pip install -r requirements.txt

Launch the Streamlit app:
streamlit run app.py

Generate a token, then scan or upload it for verification.

Vendor Reliability Scoring Module

Install dependencies (if not done):
pip install -r requirements.txt

Launch the vendor scoring app:
streamlit run vendor_app.py

Upload the sample CSV file vendors.csv to view vendor risk scores.

Next Steps

Add signature key persistence

Add vendor scoring integration into main dashboard

Integrate GPT compliance parser

Add QR scanning via camera

Combined MVP Modules

This repository currently contains two main modules:

Visual Token Authentication

Vendor Reliability Scoring

They can be run separately or will be integrated into a unified dashboard soon.
