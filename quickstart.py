from zsc.core import SemanticCipher
c = SemanticCipher()
print("ENC:", c.encrypt("hello").hex())
print("DEC:", c.decrypt(c.encrypt("hello")))
