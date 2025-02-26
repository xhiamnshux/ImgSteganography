from Crypto.Cipher import AES
import base64

KEY = b'Sixteen byte key'  # Must be 16, 24, or 32 bytes long

def encrypt_message(message):
    cipher = AES.new(KEY, AES.MODE_ECB)
    padded_message = message + ' ' * (16 - len(message) % 16)  # Pad to 16 bytes
    encrypted = cipher.encrypt(padded_message.encode())
    return base64.b64encode(encrypted).decode()

def decrypt_message(encrypted_message):
    cipher = AES.new(KEY, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted.decode().strip()

# Example Usage
secret = "Steganography"
encrypted = encrypt_message(secret)
print("Encrypted:", encrypted)
print("Decrypted:", decrypt_message(encrypted))
