import qrcode
import hashlib
import json
from datetime import datetime
from keys import private_key

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
    return token

# Required imports for cryptographic signing
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
