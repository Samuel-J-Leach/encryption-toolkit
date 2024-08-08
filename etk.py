import sys
from cryptography.fernet import Fernet

plaintext = " ".join(sys.argv[1:])

key = Fernet.generate_key()

fernet = Fernet(key)

ciphertext = fernet.encrypt(plaintext.encode()).decode("utf-8")
print("\nciphertext:\n" + ciphertext)
#plaintext = fernet.decrypt(ciphertext.encode()).decode("utf-8")
#print(plaintext)

print("\nsymmetric key:\n" + key.decode("utf-8"))

