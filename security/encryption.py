# AES/RSA + BL4CK ciphers
from cryptography.fernet import Fernet

class EncryptionSystem:
	def __init__(self):
		self.key = Fernet.generate_key()
		self.cipher = Fernet(self.key)

	def encrypt(self, data: str) -> str:
		return self.cipher.encrypt(data.encode()).decode()

	def decrypt(self, token: str) ->str:
		return self.cipher.decrypt(token.encode()).decode()
