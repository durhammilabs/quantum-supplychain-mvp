from cryptography.hazmat.primitives.asymmetric import rsa

# Generate keys once and share across modules
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()
