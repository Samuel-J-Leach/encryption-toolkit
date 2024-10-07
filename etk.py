import sys
import os
from fernet import run_fernet

def readHelpFile():
    file = open("help.txt","r")
    return file.read()

def saveOutput(command, flags, output):
    filename = "output_files/etk-"+command+"-output-"+("".join(flags))+"-"
    i = 0
    path = ""
    while True:
        try:
            file = open(filename+str(i), "x")
            file.write(output)
            path = str(os.path.abspath(filename+str(i)))
            file.close()
            break
        except:
            i += 1
            if i == 100:
                return "error"
    return "output saved to: "+path

def parseInput(args):
    command = args[1]
    flags = []
    inputs = []
    if len(args) >= 3:
        if args[2][0] == "-":
            if "s" in args[2]: flags.append("s")#save output to file
            if "k" in args[2]: flags.append("k")#take key from file
            if "i" in args[2]: flags.append("i")#take input from file
            x = 1
        else:
            x = 0
        try:
            inputs = args[2+x:]
        except:
            inputs = []
    return (command, flags, inputs)

def main():
    command, flags, inputs = parseInput(sys.argv)
    
    if command == "help":
        output =  readHelpFile()
    else:
        output = run_fernet(command, flags, inputs)
    
    if "s" in flags:
        output = output + "\n\n" + saveOutput(command, flags, output)
    return output

print("\n" + main())
#command format: python etk.py encrypt {key} message to be encrypted
