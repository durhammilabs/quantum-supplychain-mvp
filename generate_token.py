import qrcode
import hashlib
import json
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from datetime import datetime

# Generate RSA keys (in-memory for now)
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

def generate_token(shipment_id: str, origin: str, timestamp=None):
    if not timestamp:
        timestamp = datetime.utcnow().isoformat()

    payload = {
        "shipment_id": shipment_id,
        "origin": origin,
        "timestamp": timestamp
    }

    payload_bytes = json.dumps(payload).encode("utf-8")
    signature = private_key.sign(
        payload_bytes,
        padding.PKCS1v15(),
        hashes.SHA256()
    )

    token = {
        "data": payload,
        "signature": signature.hex()
    }

    qr = qrcode.make(json.dumps(token))
    qr.save("token.png")
    print("✅ Token saved as token.png")
    return token

# Example
if __name__ == "__main__":
    generate_token("SHIP12345", "Durham Distribution")
