import random


class Encryptor:
    @classmethod
    def encrypt(cls, plaintext):
        len_plaintext = len(plaintext)
        chunk_cnt = len_plaintext // 5

        if len_plaintext % 5 > 0:
            chunk_cnt += 1
            plaintext += (5 - len(plaintext) % 5) * "z"
        secret_map = random.sample(range(5), 5)

        chunks = [plaintext[5 * i: 5 * i + 5] for i in range(chunk_cnt)]
        encrypted_chunks = [["" for _ in range(5)] for _ in range(chunk_cnt)]
        for i in range(chunk_cnt):
            for j in range(5):
                encrypted_chunks[i][secret_map[j]] = chunks[i][j]

        cipher_text = ""
        for i in range(5):
            for j in range(chunk_cnt):
                cipher_text += encrypted_chunks[j][i]
        return cipher_text
