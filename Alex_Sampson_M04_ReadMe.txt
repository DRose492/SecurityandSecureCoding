Secure Text & File Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This script allows you to hash, encrypt, decrypt, sign, and verify text or files using strong cryptographic methods. It is designed to be simple to use while protecting your data's privacy, authenticity, and accessibility.

What It Does
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hashes a string or file using SHA-256 to create a unique fingerprint and encrypts text using ChaCha20, a fast and secure cipher ideal for mobile use

Decrypts text using a provided key
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Digitally signs text using ECDSA (Elliptic Curve Digital Signature Algorithm) and verifies a signature to confirm the text hasn't been tampered with

Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Before running the script, make sure you have the following Python packages installed:
 * cryptography
 * pycryptodome

You can install them using pip:
 { pip install cryptography pycryptodome }

How to Use
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Run the script in your terminal or command prompt:
 { python secure_tool.py }

You'll be prompted with a menu:
 * 1 - Hash a string
 * 2 - Hash a file
 * 3 - Encrypt text
 * 4 - Decrypt text
 * 5 - Sign text
 * 6 - Verify signature
 * 0 - Exit

Type the number of the action you want to perform and follow the instructions.

Security Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Keys and nonces are generated using secure random values (os.urandom) to ensure strong protection. Do not reuse nonces with the same key when encrypting multiple messages. Keep your keys safe—they're printed for demonstration but should be stored securely in real applications.

Why It Matters
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This script helps protect your data by keeping it private, making sure it hasn’t been changed, and ensuring it works when you need it. It uses randomness (entropy) to make encryption keys unpredictable, which is critical for strong security.