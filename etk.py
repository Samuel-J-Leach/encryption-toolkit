import sys
from fernet import run_fernet

def readHelpFile():
    file = open("help.txt","r")
    return file.read()

def main():
    command = sys.argv[1]
    if command == "help":
        output = readHelpFile()
    elif command == "fernet":
        output = run_fernet(sys.argv[2:])
    elif command == "rsa":
        output = "this feature has not been implemented yet"
    else:
        output = "ERROR: command '"+command+"' not recognised, enter 'python etk.py help' for a list of valid commands"
    return output

print("\n" + main())
