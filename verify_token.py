import json
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def verify_token(token: dict, public_key):
    payload_bytes = json.dumps(token["data"]).encode("utf-8")
    signature = bytes.fromhex(token["signature"])

    try:
        public_key.verify(
            signature,
            payload_bytes,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False
