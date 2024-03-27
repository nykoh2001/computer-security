class Decryptor:
    with open('../words.txt') as f:
        words = [w.rstrip().lower() for w in f.readlines()]

    @classmethod
    def decrypt(cls, ciphertext):
        with open("decrypted.txt", 'a') as f:
            for key in range(1, 26):
                plain_text = ""
                for char in ciphertext:
                    if char.isalpha():
                        ascii_val = ord(char) - key
                        if ascii_val < ord('a'):
                            ascii_val += 26
                        plain_text += chr(ascii_val)
                    else:
                        plain_text += char
                plain_words = plain_text.split(" ")

                is_answer = True
                for word in plain_words:
                    if word not in cls.words:
                        is_answer = False
                        break
                if is_answer:
                    f.write("\n***** Answer *****\n")
                    f.write("Encrypt Key: " + str(key) + "\n")
                    f.write(ciphertext)
                    f.write("\nmeans >> " + plain_text + "\n\n")