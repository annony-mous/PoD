from ecdsa import VerifyingKey, SECP256k1
from signing import sign_file
import hashlib

# PUBLIC_KEY_HEX = "04c83c04b482b7b86402f539a3c1ea80d5c5dbe941abb33cd3e2e15dc72b5f2fd56fa2ea21a1a12bdf93b5a85341dc3cd71ddf4c82f7b5eb4b57293867dd60bf30" # M1
PUBLIC_KEY_HEX = "04614e06fe6aca94f78341b5fded84fe8c478bed8fa5ba129a650581f1e9289d5b17791c3a764e4259966881020abc1d002b3a7c89d4f9511e94b7bc9842f4788d" # M2

def verify_file(filepath, signature_hex):
    vk = VerifyingKey.from_string(bytes.fromhex(PUBLIC_KEY_HEX), curve=SECP256k1)

    with open(filepath, "rb") as f:
        data = f.read()

    file_hash = hashlib.sha256(data).digest()
    signature = bytes.fromhex(signature_hex)

    return vk.verify(signature, file_hash)


fileName = "competition.md"
signature = sign_file(fileName)
print(verify_file(fileName, signature))