from ecdsa import SigningKey, SECP256k1
import hashlib

# ⚠️ DO NOT hardcode real private keys in real projects
PRIVATE_KEY_HEX = hex(41277428321077118207198481920533738504513433332821919708143902735601246915662)[2:]

def sign_file(filepath):
    # Load private key
    sk = SigningKey.from_string(bytes.fromhex(PRIVATE_KEY_HEX), curve=SECP256k1)
    # Read file
    with open(filepath, "rb") as f:
        data = f.read()

    # Hash file (recommended)
    file_hash = hashlib.sha256(data).digest()

    # Sign hash
    signature = sk.sign(file_hash)

    return signature.hex()

if __name__ == "__main__":
    file_path = "competition.md"
    signature = sign_file(file_path)

    print("File signature (hex):")
    print(signature)
