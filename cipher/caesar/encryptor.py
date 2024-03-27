import random


class Encryptor:

    @classmethod
    def encrypt(cls, plaintext):
        encrypt_key = random.randint(1, 25)
        cipher_text = ""
        for char in plaintext:
            if char.isalpha():
                ascii_val = ord(char) + encrypt_key
                if ascii_val > ord('z'):
                    ascii_val -= 26
                cipher_text += chr(ascii_val)
            else:
                cipher_text += char
        return cipher_text
