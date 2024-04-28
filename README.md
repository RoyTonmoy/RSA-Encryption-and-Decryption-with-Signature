
# RSA Encryption/Decryption and Signature Verification

## Project Description
This repository contains Python scripts for implementing RSA encryption and decryption, along with signature generation and verification. RSA (Rivest–Shamir–Adleman) is one of the first public-key cryptosystems and is widely used for secure data transmission. The project is divided into several modules, each handling specific aspects of RSA functionality.

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
