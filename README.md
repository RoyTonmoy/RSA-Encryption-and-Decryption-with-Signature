
# RSA Encryption/Decryption and Signature Verification

## Project Description

RSA(Rivest-Shamir-Adleman) is one of the earliest public-key cryptosystems and is widely used for secure data transmission. Here’s an explanation of its main components and how it works:

### Key Components of RSA:
1. **Key Generation**:
   - **Public and Private Keys**: RSA involves a set of two keys: a public key, which can be distributed widely, and a private key, which must be kept secret.
   - **Prime Numbers and Modulus**: The keys are generated from two large prime numbers. These primes are used to compute the modulus (n = pq) which is part of both the public and the private keys.
   - **Public Exponent and Private Exponent**: The public key also includes an exponent (e), which is typically chosen to satisfy certain mathematical properties for efficient encryption and decryption. The private key includes a different exponent (d), calculated to be the modular multiplicative inverse of e modulo (p-1)(q-1).

2. **Encryption**:
   - Using the recipient’s public key (which includes n and e), data can be encrypted. Anyone can encrypt data using the public key, but only the holder of the private key can decrypt it.

3. **Decryption**:
   - The private key, which contains the modulus n and the private exponent d, is used to decrypt data. The mathematical properties of d allow the holder to efficiently compute the original message from the encrypted data.

### How RSA Works:
1. **Key Generation**:
   - Select two large prime numbers, p and q.
   - Calculate n = p * q. This n is used as the modulus for both the public and private keys.
   - Compute φ(n) = (p-1) * (q-1), where φ is Euler's totient function.
   - Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1; e and φ(n) must be coprime.
   - Determine d as d ≡ e^(-1) (mod φ(n)); d is the modular multiplicative inverse of e modulo φ(n).

2. **Encryption Process**:
   - Convert the plaintext message into an integer m (0 < m < n).
   - The ciphertext c is created using the formula c ≡ m^e (mod n).

3. **Decryption Process**:
   - The original message m is recovered by computing m ≡ c^d (mod n).

### Security:
- RSA’s security relies on the difficulty of factoring the product of two large prime numbers. The larger these primes are, the more secure the RSA system is.
- The use of large key sizes (e.g., 2048 bits or more) is recommended to ensure security against modern computational power.

### Applications:
- **Data Encryption**: RSA is used to encrypt data, ensuring that sensitive information can be transmitted securely over unsecured networks.
- **Digital Signatures**: RSA is also used for digital signatures, which verify the authenticity and integrity of digital documents.

RSA is a fundamental tool in digital security, used in a variety of applications from secure web browsing (via HTTPS) to securing emails and digitally signing software and documents.


## File Structure
- `RSAKey.py` - Generates RSA keys and provides functions for key management.
- `Encryption.py` - Handles the encryption of messages using RSA public keys.
- `Decryption.py` - Manages decryption of messages using RSA private keys.
- `SignatureVerification.py` - Allows signing messages and verifying signatures using RSA keys.

## Requirements
- Python 3.x
- No external libraries are required for the basic functionality.

## Usage

### Generating Keys
Run `RSAKey.py` to generate a pair of RSA keys. The keys will be used for encryption, decryption, and signing of messages.
```bash
python RSAKey.py
```

### Encrypting a Message
Use `Encryption.py` to encrypt messages. The script will prompt you to enter the plaintext message and then display the encrypted message.
```bash
python Encryption.py
```

### Decrypting a Message
`Decryption.py` is used to decrypt messages encrypted by the RSA algorithm. Input the encrypted message when prompted.
```bash
python Decryption.py
```

### Signing a Message
To sign a message, run `SignatureVerification.py` and choose the option to sign the message. Follow the on-screen prompts to enter the message and obtain the signature.
```bash
python SignatureVerification.py
```

### Verifying a Signature
Run `SignatureVerification.py`, choose the verification option, and enter the signature values. The script will verify if the signature matches the expected message.
```bash
python SignatureVerification.py
```

## Important Notes
- Ensure that you are using securely generated keys and handling them properly to maintain security.
- This implementation is for educational purposes and might not be secure for production environments without further security measures.
