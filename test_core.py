from zsc.core import SemanticCipher

def test_roundtrip():
    c = SemanticCipher()
    msg = "bonjour zoran"
    enc = c.encrypt(msg)
    dec = c.decrypt(enc)
    assert dec == msg
