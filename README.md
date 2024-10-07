# encryption-toolkit

uses the cryptography module for python.

encrypts/decrypts files and simple strings.

command format: python etk.py operation -flags {key} input data

flags:
- s: save output to file
- k: key is filepath to actual key
- i: input data is filepath to actual input data

command examples in cmd:<br>
cmd> python etk.py help<br>
cmd> python etk.py key<br>
cmd> python etk.py encrypt {OKTi0Q9h74NgyfzsAeXX0_9mbJL2djifY5W-LkVySRM=} message to be encrypted<br>
etc...
