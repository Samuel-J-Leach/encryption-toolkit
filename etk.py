import sys
from fernet import run_fernet

def readHelpFile():
    file = open("help.txt","r")
    return file.read()

def main():
    command = sys.argv[1]
    if command == "help":
        return readHelpFile()

    flags = []
    inputs = []
    if len(sys.argv) >= 3:
        if sys.argv[2][0] == "-":
            if "s" in sys.argv[2]: flags.append("s")#save output to file
            if "k" in sys.argv[2]: flags.append("k")#take key from file
            if "i" in sys.argv[2]: flags.append("i")#take input from file
            inputs = sys.argv[3:]
        else:
            inputs = sys.argv[2:]
        
    output = run_fernet(command, flags, inputs)
    return output

print("\n" + main())
#command format: python etk.py encrypt {key} message to be encrypted
