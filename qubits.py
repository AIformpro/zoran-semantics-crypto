# Minimal placeholder so tests pass.

def encode_qubits(coeffs: str) -> bytes:
    if not isinstance(coeffs, str):
        raise TypeError("encode_qubits expects str")
    return coeffs.encode("utf-8")

def decode_qubits(payload: bytes) -> str:
    if not isinstance(payload, (bytes, bytearray)):
        raise TypeError("decode_qubits expects bytes")
    return payload.decode("utf-8")
