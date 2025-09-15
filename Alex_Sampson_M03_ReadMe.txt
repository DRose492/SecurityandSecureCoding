This is a Python script that allows users to:

- Hash a string or file using SHA-256
- Encrypt and decrypt text using ChaCha20
- Sign and verify text using ECDSA digital signatures

The script runs in the console and provides a menu for user interaction.

Requirements:
- Python 3.10 or higher
- Internet connection (used to install the cryptography package automatically if missing)

How to run:
1. Download the script file
2. Open a terminal and navigate to the folder containing the script
3. Run the script

The script will install the required cryptography package automatically if it's not already installed.

Notes:
- ChaCha20 uses a fixed key and nonce in this script for simplicity. This is not secure for real-world use.
- Keys for digital signatures are generated fresh each time the script runs. They are not saved.
- File hashing assumes the file exists and is readable. If not, an error message is shown.

And an additional author note, this is my first time using and learning ChaCha20, but I wanted to use a cipher that was a little more complex than Ceasar Cipher. So parden me for any bugs or failed logic because I'm trying to wrap my head around it.