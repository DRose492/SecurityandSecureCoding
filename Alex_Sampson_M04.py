"""
A script to hash a text string or file into SHA-256 hash, encrypt it using the ChaCha20, mainly because it has mobile capabilities.

This section below once auto-installed the required libraries for the script to function.
At the recommendation of others, I have removed that system and created a function to check to see if the required functions were installed.
I set their importation after the function so that the script doesn't error trying to import from libraries that haven't been verified to be there
"""
import sys
import hashlib
import os

def ReqPackageCheck(packages):
    missing = []
    for pkg in packages:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)

    if missing:
        sys.stderr.write(
            "Missing required packages:\n" +
            "\n".join(f"  - {pkg}" for pkg in missing) +
            "\nPlease install them manually before running this script.\n"
        )
        sys.exit(1)

ReqPackageCheck(['cryptography', 'pycryptodome'])

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature
"""
Now to create the functions for hashing strings and files
"""
def hash_string(text):
    sha = hashlib.sha256()
    sha.update(text.encode('utf-8'))
    return sha.hexdigest()

def hash_file(filename):
    sha = hashlib.sha256()
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            sha.update(chunk)
    return sha.hexdigest()

"""
Now to build the functions for ChaCha20
"""

def encrypt(text):
    key = os.urandom(32)    # 256-bit key
    nonce = os.urandom(12)  # 96-bit nonce NOTE: In real applications, never reuse nonce with the same key!
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(text.encode('utf-8'))
    print(key)
    print("this key is used to decript this code")
    return encrypted

def decrypt(encrypted_bytes):
    nonce = os.urandom(12)
    key = input("Please type in your key ")
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted_bytes)
    return decrypted.decode('utf-8')

"""
Now to build the digital signiture function
"""
private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
public_key = private_key.public_key()

def sign_data(data):
    signature = private_key.sign(data, ec.ECDSA(hashes.SHA256()))
    return signature

def verify_signature(data, signature):
    try:
        public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False

"""
Now for the logic so that users can interact with the script
"""
print("Please make a selection")

while True:
    print("\nChoose an option:")
    print("1 - Hash a string")
    print("2 - Hash a file")
    print("3 - Encrypt text")
    print("4 - Decrypt text")
    print("5 - Sign text")
    print("6 - Verify signature")
    print("0 - Exit")

    choice = input("Your choice: ")

    if choice == "1":
        text = input("Enter text to hash: ")
        print("SHA-256 Hash:", hash_string(text))

    elif choice == "2":
        path = input("Enter file path: ")
        print("SHA-256 File Hash:", hash_file(path))

    elif choice == "3":
        text = input("Enter text to encrypt: ")
        encrypted = encrypt(text)
        print("Encrypted bytes:", encrypted)
        # Save for later decryption
        global last_encrypted
        last_encrypted = encrypted

    elif choice == "4":
        try:
            decrypted = decrypt(last_encrypted)
            print("Decrypted text:", decrypted)
        except NameError:
                print("No encrypted text found. Please encrypt something first.")

    elif choice == "5":
        text = input("Enter text to sign: ")
        signature = sign_data(text.encode('utf-8'))
        global last_signature
        last_signature = signature
        global last_signed_text
        last_signed_text = text
        print("Signature:", signature)

    elif choice == "6":
        try:
            valid = verify_signature(last_signed_text.encode('utf-8'), last_signature)
            print("Signature valid:", valid)
        except NameError:
            print("No signature found. Please sign something first.")

    elif choice == "0":
        print("Goodbye, Alex!")
        break

    else:

        print("Invalid choice. Try again.")

