import sys
from cryptography.fernet import Fernet

FORMAT = "utf-8"

def encrypt(key, plaintext):
    fernet = Fernet(key.encode())
    return fernet.encrypt(plaintext.encode()).decode(FORMAT)

def decrypt(key, ciphertext):
    fernet = Fernet(key.encode())
    return fernet.decrypt(ciphertext.encode()).decode(FORMAT)

def create_key():
    return Fernet.generate_key().decode(FORMAT)

def readHelpFile():
    file = open("help.txt","r")
    return file.read()

def main():
    operation = sys.argv[1]
    if operation == "help":
        output = readHelpFile()
    elif operation == "encrypt":
        output = encrypt(sys.argv[2], " ".join(sys.argv[3:]))
    elif operation == "decrypt":
        output = decrypt(sys.argv[2], " ".join(sys.argv[3:]))
    elif operation == "key":
        output = create_key()
    else:
        output = "ERROR: operation not recognised, enter 'python etk.py help' for a list of valid operations"
    return output

print("\n" + main())
#" ".join(sys.argv[2:])
