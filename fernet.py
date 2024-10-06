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

def run_fernet(operation, flags, args):
    kstart = -1
    kend = -1
    for i in range(len(args)):
        if args[i][0] == "{": kstart = i
        if args[i][len(args[i])-1] == "}": kend = i+1

    if (kstart == -1 or kend == -1 or kstart >= kend) and operation != "key": return "ERROR: command format is incorrect.\nEnter 'python etk.py help' for help"
    
    if "k" in flags:
        key = (open(" ".join(args[kstart:kend]))).read()
    else:
        key = " ".join(args[kstart:kend])

    if "i" in flags:
        data = (open(" ".join(args[kend:]))).read()
    else:
        data = " ".join(args[kend:])
    
    if operation == "encrypt":
        output = encrypt(key, data)
    elif operation == "decrypt":
        output = decrypt(key, data)
    elif operation == "key":
        output = create_key()
    else:
        output = "ERROR: operation '"+operation+"' not recognised.\nEnter 'python etk.py help' for a list of valid operations"
    return output
