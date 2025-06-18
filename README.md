# Quantum Supply Chain MVP

This repository contains two key modules for a supply chain optimization and verification platform:

- **Visual Token Authentication:** Secure QR-style tokens that verify shipment authenticity using cryptographic signatures.
- **Vendor Reliability Scoring:** AI-driven system to score vendors based on shipment history and geopolitical risk.

---

## How to Run

### Token Authentication Module

```bash
git clone https://github.com/durhammilabs/quantum-supplychain-mvp.git
cd quantum-supplychain-mvp
pip install -r requirements.txt
streamlit run app.py

pip install -r requirements.txt
streamlit run vendor_app.py


Next Steps
Add signature key persistence

Integrate vendor scoring into the main dashboard

Build GPT compliance parsing module

Add QR scanning via camera

Combined MVP Modules
This repository currently contains two main modules:

Visual Token Authentication

Vendor Reliability Scoring

They can be run separately or will be integrated into a unified dashboard soon.

