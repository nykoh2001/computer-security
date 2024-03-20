import string
import time
import hashlib
from itertools import product
from hash_function import HashFunction


class BruteForceAttacker:
    def __init__(self, type: int, length: int, hash: str):
        self._type = type
        self.length = length
        self.hash_func = HashFunction(hash)
        if self._type == 1:
            self.letter_set = string.digits
        elif self._type == 2:
            self.letter_set = string.ascii_letters
        elif self._type == 3:
            self.letter_set = string.digits + string.ascii_letters
        elif self._type == 4:
            self.letter_set = string.digits + string.ascii_letters + string.punctuation
        else:
            raise ValueError("Invalid type number")

    def attack(self, hash_answer):
        start = time.time()
        all_passwd = list(product(self.letter_set, repeat=self.length))
        for password in all_passwd:
            if self.hash_func("".join(password)) == hash_answer:
                print("cracked password:", "".join(password))
                print("cracking time:", time.time() - start)
                return
        print("Cracking Failed")
        print("cracking time:", time.time() - start)
        return
