def convertToHexadecimal(message):
    chunkLen = 3     #defining size of chunk is 3
    chunks = []      #will store all the chunk in this list
    hexaList = []    #will store all the hexaDecimal value here


    for i in range(0, len(message), chunkLen):
        chunk = message[i:i+chunkLen]
        chunks.append(chunk)
    
    print(chunks)

    for chunk in chunks:
        # print(chunk)
        hexaText = '' 
        
        for char in chunk:
            # print(char)
            hexaDecimal_value = hex(ord(char))[2:]
            hexaText += hexaDecimal_value
        hexaList.append(hexaText)
    
    return hexaList


def squareAndMultiply(m, e, n):
    sm_value = 1
    binary_e = bin(e)[2:]
    # print(binary_e)

    for bit in binary_e:
        sm_value = (sm_value * sm_value) % n
        # print("sm%n: ", sm_value)

        if bit == '1':
            sm_value = (sm_value * m) % n
            # print("if bit: ", sm_value)

    return sm_value


def encryptRSA(plainText, e, N):
    hexaDecimalValues = convertToHexadecimal(plainText)
    encryptedText = []

    for hex_value in hexaDecimalValues:
        decimal = int(hex_value, 16)
        print(decimal)
        encryptedMsg = squareAndMultiply(decimal, e, N)
        encryptedText.append(encryptedMsg)
    
    return encryptedText

    
plain_text = input("Enter your message to encrypt in RSA: ")

# my N, e
# e = 79307
# N = 1372514879

# my partners N and e
e=2291269535
N=2859388031

# N = 2539109269
# e = 67


cipherText = encryptRSA(plain_text, e, N)
print("Encrypted message: ",cipherText)
