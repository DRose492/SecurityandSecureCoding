Playfair Cipher Script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Purpose
~~~~~~~~~~~~~~~~~~~~
This script lets you encrypt or decrypt messages using the Playfair Cipher, a classical encryption method.

How it Works
~~~~~~~~~~~~~~~~~~~~
 * You choose whether to encrypt or decrypt.
 * You enter a keyword, which is used to build a 5×5 letter grid.
 * Your message is split into pairs of letters.
 * The script applies the Playfair rules:
      1. Same row → shift right (or left when decrypting).
      2. Same column → shift down (or up when decrypting).
      3. Rectangle → swap corners.

The result is shown as grouped text (encryption) or plain text (decryption).