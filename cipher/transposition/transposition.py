import time

from sentence_generator import SentenceGenerator
from encryptor import Encryptor
from decryptor import Decryptor


def main():
    avg_time = 0
    for i in range(100):
        start_time = time.time()
        sentence = SentenceGenerator.generate()
        print("sentence:", sentence)

        ciphertext = Encryptor.encrypt(sentence)
        print("cipher text:", ciphertext, "\n")
        Decryptor.decrypt(ciphertext, sentence)
        avg_time += time.time() - start_time
    print("average encrypt/decrypt time:", avg_time / 100)


if __name__ == "__main__":
    main()
