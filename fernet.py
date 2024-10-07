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

#determines which items in args make up the key
def findKey(args):
    start = -1
    end = -1
    for i in range(len(args)):
        if args[i][0] == "{": start = i
        if args[i][len(args[i])-1] == "}": end = i+1
    return (start, end)

#either retrieves key from args or from a file
def retrieveKey(flags, args, start, end):
    if "k" in flags:
        path = " ".join(args[start:end])
        key = (open(path[1:len(path)-1])).read()
    else:
        key = " ".join(args[start:end])
        key = key[1:len(key)-1]
    return key

#either retrieves input data from args or from a file
def retrieveData(flags, args, start):
    if "i" in flags:
        data = (open(" ".join(args[start:]))).read()
    else:
        data = " ".join(args[start:])
    return data

def run_fernet(operation, flags, args):
    
    kstart, kend = findKey(args)
    if (kstart == -1 or kend == -1 or kstart >= kend) and operation != "key":
        output = "ERROR: command format is incorrect.\nEnter 'python etk.py help' for help"
    else:
        key = retrieveKey(flags, args, kstart, kend)
        data = retrieveData(flags, args, kend)
        
        if operation == "encrypt":
            output = encrypt(key, data)
        elif operation == "decrypt":
            output = decrypt(key, data)
        elif operation == "key":
            output = create_key()
        else:
            output = "ERROR: operation '"+operation+"' not recognised.\nEnter 'python etk.py help' for a list of valid operations"
    
    return output
