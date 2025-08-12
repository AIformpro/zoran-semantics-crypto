import base64
from .wavelets import forward, inverse
from .qubits import encode_qubits, decode_qubits

class SemanticCipher:
    def encrypt(self, text: str) -> bytes:
        coeffs = forward(text)
        return encode_qubits(coeffs)

    def decrypt(self, payload: bytes) -> str:
        coeffs = decode_qubits(payload)
        return inverse(coeffs)

def main():
    import sys
    c = SemanticCipher()
    if len(sys.argv) >= 3 and sys.argv[1] == "enc":
        out = c.encrypt(" ".join(sys.argv[2:]))
        print(base64.b64encode(out).decode())
    elif len(sys.argv) == 3 and sys.argv[1] == "dec":
        try:
            raw = base64.b64decode(sys.argv[2])
        except Exception:
            print("Invalid base64 payload", file=sys.stderr)
            sys.exit(1)
        print(c.decrypt(raw))
    else:
        print("Usage: zsc enc <text> | zsc dec <b64>")
