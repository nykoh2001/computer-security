from itertools import permutations


class Decryptor:
    @classmethod
    def decrypt(cls, ciphertext, plaintext):
        len_ciphertext = len(ciphertext)

        chunk_cnt = len_ciphertext // 5
        chunks = ["" for _ in range(chunk_cnt)]
        for i in range(chunk_cnt):
            for j in range(5):
                chunks[i] += ciphertext[chunk_cnt * j + i]

        unshuffled_chunks = [["" for _ in range(5)] for _ in range(chunk_cnt)]
        secret_maps = list(permutations([i for i in range(5)], 5))
        for secret_map in secret_maps:
            for i in range(chunk_cnt):
                for j in range(5):
                    unshuffled_chunks[i][secret_map[j]] = chunks[i][j]

            decrypted_text = "".join(["".join(unshuffled_chunks[i]) for i in range(chunk_cnt)])
            if plaintext in decrypted_text:
                with open("decrypted.txt", 'a') as f:
                    f.write("\n***** Answer *****\n")
                    f.write("Encrypt Key: " + str(secret_map) + "\n")
                    f.write(ciphertext)
                    f.write("\nmeans >> " + plaintext + "\n\n")
