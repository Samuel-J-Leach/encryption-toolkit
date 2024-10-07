# encryption-toolkit

uses the cryptography module for python.

encrypts/decrypts files and simple strings.

command general format: python etk.py operation -flags {key} input data

flags:
- s: save output to file
- k: key is filepath to actual key
- i: input data is filepath to actual input data

operations:
- help: displays a list of operations
- key: creates a fernet key
- encrypt: uses a fernet key to encrypt plaintext
- decrypt: uses a fernet key to decrypt ciphertext

command examples in cmd:<br>
cmd> python etk.py help<br>
cmd> python etk.py key<br>
cmd> python etk.py key -s<br>
cmd> python etk.py encrypt {OKTi0Q9h74NgyfzsAeXX0_9mbJL2djifY5W-LkVySRM=} message to be encrypted<br>
cmd> python etk.py encrypt -k {key_file.txt} message to be encrypted<br>
cmd> python etk.py encrypt -ki {key_file.txt} encrypted_file.txt<br>
etc...
