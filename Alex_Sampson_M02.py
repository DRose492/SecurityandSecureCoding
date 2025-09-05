# A script for encrypting and decripting messaging using the Playfair Cipher


# The following variables are global variables
Text = ""       # Grabs thephrase to be encrypted/decrypted
Keyword = ""    # The Keyword/phrase to be used to create the grid
i = 0           # A variable used in multiple functions for interation count
Inquiry = ""    # Non-important user inquiry
Encrypt = False
Decrypt = False


# Inquire what the user is trying to do (Encrypt or Decrypt)
while True:
    Inquiry = input("Are you looking to encrypt or decrypt a message? ")
    Inquiry = Inquiry.lower().split()

    for word in Inquiry:
        if word == "encrypt":
            Encrypt = True
            break
        elif word == "decrypt":
            Decrypt = True
            break
    else:
        print("I'm sorry. I didn't catch that. Please try again. ")
        continue

    break


# Let's get the grid built for either the encription or decryption
Keyword = input("What keyword or keyphrase are we using? ")

def Grid(Keyword):
    Keyword = Keyword.upper().replace("J", "I")
    Seen = set()
    Grid_Temp= []

    for char in Keyword:
        if char not in Seen and char.isalpha():
            Seen.add(char)
            Grid_Temp.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in Seen:
            Seen.add(char)
            Grid_Temp.append(char)

    Rows = [Grid_Temp[i:i+5] for i in range (0, 25, 5)]

    return Rows

Grids = Grid(Keyword)


# Retrieve and format the text to be encrypted/decrypted
Text = input("\n What text do you want to encrypt/decrypt? ")

def Input_Format(Text):
    Text = Text.upper().replace("J","I").replace(" ","")
    Text02 = ""
    for char in Text:
        if char.isnumeric() or not char.isalpha():
            Text02 += char * 2
        else:
            Text02 += char
    Text = Text02
    Pairs = []
    i = 0

    while i < len(Text):
        a = Text[i]
        if (i + 1) < len(Text) and Text[i + 1].isalpha():
            b = Text[i + 1]
            if a == b:
                Pairs.append((a, "Z"))
                i += 1
            else:
                Pairs.append((a, b))
                i += 2
        elif (i + 1) < len(Text) and not a.isalpha() and not Text[i + 1].isalpha():
            b = Text[i + 1]
            Pairs.append((a, b))
            i += 2
        else:
            Pairs.append((a, "Z"))
            i += 1

    return Pairs

Pairs = Input_Format(Text)


# Now to define the function to find positions on the grid
def Position(Grids):
    Position_dict = {}
    for row in range(5):
        for col in range(5):
            Position_dict[Grids[row][col]] = (row, col)

    return Position_dict

# Now to encrypt the pairs of characters
def Encrypter(Pairs, Grids):
    Position_dict = Position(Grids)
    Encrypted_Text = ""

    for a, b in Pairs:
        if not (a.isalpha() and b.isalpha()):
            Encrypted_Text += a
            continue
        else:
            Row1, Col1 = Position_dict[a]
            Row2, Col2 = Position_dict[b]

            if Row1 == Row2:                                    # Rule 1 of the Playfair Cipher, if the two letters are located in the same row
                Encrypted_Text += Grids[Row1][(Col1 + 1) % 5]    # Shift both letters over one position to the right, wrapping around as needed.
                Encrypted_Text += Grids[Row2][(Col2 + 1) % 5]
            elif Col1 == Col2:                                  # Rule 2 of the Cipher, if the two letters are located in the same column
                Encrypted_Text += Grids[(Row1 + 1) % 5][Col1]    # Shift both letters down one position, wrapping around as needed.
                Encrypted_Text += Grids[(Row2 + 1) % 5][Col2]
            else:                                               # Rule 3 of the Cipher, if both letters are two corners of a rectangle
                Encrypted_Text += Grids[Row1][Col2]              # Replace that letter with the opposite corner within that same row.
                Encrypted_Text += Grids[Row2][Col1]

    return Encrypted_Text

# And now to decrypt them
def Decrypter(Pairs, Grids):
    Position_dict = Position(Grids)
    Encrypted_Text = ""

    for a, b in Pairs:
        if not (a.isalpha() and b.isalpha()):
            Encrypted_Text += a
            continue
        else:
            Row1, Col1 = Position_dict[a]
            Row2, Col2 = Position_dict[b]

            if Row1 == Row2:                                    # Rule 1 of the Playfair Cipher, if the two letters are located in the same row
                Encrypted_Text += Grids[Row1][(Col1 - 1) % 5]    # Shift both letters over one position to the right, wrapping around as needed.
                Encrypted_Text += Grids[Row2][(Col2 - 1) % 5]
            elif Col1 == Col2:                                  # Rule 2 of the Cipher, if the two letters are located in the same column
                Encrypted_Text += Grids[(Row1 - 1) % 5][Col1]    # Shift both letters down one position, wrapping around as needed.
                Encrypted_Text += Grids[(Row2 - 1) % 5][Col2]
            else:                                               # Rule 3 of the Cipher, if both letters are two corners of a rectangle
                Encrypted_Text += Grids[Row1][Col2]              # Replace that letter with the opposite corner within that same row.
                Encrypted_Text += Grids[Row2][Col1]

    return Encrypted_Text

# Now to increase the security of the cipher by formating the output
def Output_Format(New_Text):
    Grouped_Text = " ".join([New_Text[i: i + 4] for i in range(0, len(New_Text), 4)])

    return Grouped_Text

for row in Grids:
    print(" ".join(row))

while Encrypt is True:
    New_Text = Encrypter(Pairs, Grids)
    New_Text = Output_Format(New_Text)
    print(New_Text)
    Encrypt = False

while Decrypt is True:
    New_Text = Decrypter(Pairs, Grids)
    New_Text = New_Text.replace("Z", "")
    New_Text = "".join(New_Text)
    print(New_Text)
    Decrypt = False
