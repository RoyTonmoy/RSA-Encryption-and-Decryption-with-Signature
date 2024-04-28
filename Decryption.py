def mergeText(ctext):
    text_ascii = []
    
    for i in range(0, len(ctext)):
        hexaDecimal_value = hex(ctext[i])[2:]
        try:
            ascii_char = bytearray.fromhex(hexaDecimal_value).decode()
            text_ascii.append(ascii_char)
        except ValueError:
            text_ascii.append('*')

    print("Decrypted message in chunks = ", text_ascii)
    PlainText = "".join(text_ascii)
    print("PlainText: ", PlainText)
    return PlainText


def square_multiply(m, e, n):
    sm_value = 1
    binary_e = bin(e)[2:]

    for bit in binary_e:
        sm_value = (sm_value * sm_value) % n

        if bit == '1':
            sm_value = (sm_value * m) % n

    return sm_value

# Function to decrypt the ciphertext using RSA
def decryption(c_text, d, n):
    try:
        ciphertext = []   # Create an empty list to store decrypted ciphertext
    
        # Loop through the ciphertext list
        for i in range(0, len(c_text)):
            ciphertext.append(square_multiply(c_text[i], d, n)) # m = c^d mod N

        # Return the decrypted ciphertext
        return ciphertext
    except TypeError as e:
        print(e)  # Print any TypeError that might occur during decryption


def inputFunction():
    cipher_text = input("Cipher text = ")
    print(type(cipher_text))
    cipher_text = cipher_text.replace("[", "")  # Removing '['
    cipher_text = cipher_text.replace("]", "")  # Removing ']'
    cipher_text = list(map(int, cipher_text.split(',')))  # Split the string by ',' and convert elements to integers
    print("Splited text: ", cipher_text)

    return cipher_text


# RSA private key components
e = 79307
n = 1372514879
d = 453799907


# calling user input function

cipher_text = inputFunction()

# Decrypt the ciphertext using the RSA decryption function
m = decryption(cipher_text, d, n)

# Display the decrypted message
print("\n----------------RSA Decryption----------------")
print("Decrypted message = ", mergeText(m))
