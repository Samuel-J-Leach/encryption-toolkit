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

def run_fernet(args):
    operation = args[0]
    if operation == "encrypt":
        output = encrypt(args[1], " ".join(sys.argv[2:]))
    elif operation == "decrypt":
        output = decrypt(args[1], " ".join(sys.argv[2:]))
    elif operation == "key":
        output = create_key()
    else:
        output = "ERROR: operation '"+operation+"' not recognised, enter 'python etk.py help' for a list of valid operations"
    return output
