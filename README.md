# Quantum Supply Chain MVP: Visual Token Auth

This is the first module of the supply chain system — a secure QR-style token that verifies shipment authenticity using cryptographic signatures.

## How to Run

1. Clone the repo:
   ```
   git clone https://github.com/durhammilabs/quantum-supplychain-mvp.git
   cd quantum-supplychain-mvp
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Launch the Streamlit app:
   ```
   streamlit run app.py
   ```

4. Generate a token, scan or upload it for verification.

---

## Next Steps

- Add signature key persistence
- Add vendor scoring module
- Integrate GPT compliance parser
- Use QR scanning via camera


---

## Vendor Reliability Scoring Module

This module provides a simple AI-driven system to score vendors based on shipment history and geopolitical risk.

- **`vendors.csv`** — Sample vendor dataset with performance metrics  
- **`vendor_risk.py`** — Python module that computes risk scores from the dataset  
- **`vendor_app.py`** — Streamlit app to upload vendor data and visualize risk levels with color-coded risk scores

### How to Run

```bash
pip install -r requirements.txt
streamlit run vendor_app.py
