def convertToHexadecimal(message):
    chunkLen = 3     #defining size of chunk is 3
    chunks = []      #will store all the chunk in this list
    hexaList = []    #will store all the hexaDecimal value here


    for i in range(0, len(message), chunkLen):
        chunk = message[i:i+chunkLen]
        chunks.append(chunk)
    
    print(chunks)

    for chunk in chunks:
        hexaText = '' 
        
        for char in chunk:
            hexaDecimal_value = hex(ord(char))[2:]
            hexaText += hexaDecimal_value
        hexaList.append(hexaText)
    
    return hexaList


def square_multiply(m, e, n):
    sm_value = 1
    binary_e = bin(e)[2:]

    for bit in binary_e:
        sm_value = (sm_value * sm_value) % n

        if bit == '1':
            sm_value = (sm_value * m) % n

    return sm_value


def sign(s_text, d, n):
    c = []
    c = convertToHexadecimal(s_text)
    signedtext = []
    l = len(c)
    x = 0
    while (x < l):
        m = int(c[x], 16)
        signedtext.append(square_multiply(m, d, n))
        x = x + 1
    return signedtext


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


def verify(c_text, e, n):
    try:
        signtext = []
        l = len(c_text)
        s = 0
        while (s < l):
            signtext.append(square_multiply(c_text[s], e, n))
            s = s + 1
        return signtext
    except TypeError as e:
        print(e)


while True:
    print("To generate a signature, press 1")
    print("To verify a signature, press 2")
    print("To exit, press 0")

    choice = input("Enter your choice: ")

    if choice == "1":
        message_to_sign = input("Enter the message to be signed: ")
        n = 1744751251
        d = 220379039
        signature = sign(message_to_sign, d, n)

        print("RSA Signature:", signature)

    elif choice == "2":
        partner_signature = input("Enter partner signature (comma-separated values): ")

        partner_signature = partner_signature.replace('[', '').replace(']', '')

        partner_signature = [int(i) for i in partner_signature.split(',')]

        n = 168618547
        e = 35201

        verified_signature = verify(partner_signature, e, n)

        verified_message = mergeText(verified_signature)

        origninal_message = "Dinesh Nagalingam"

        if verified_message == origninal_message:
            print("The signature is True. Accept the message.")
        else:
            print("The signature is False. Don't accept the message.")

    elif choice == "0":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 0, 1, or 2.")