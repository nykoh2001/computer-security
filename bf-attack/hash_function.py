import hashlib
from ascii_hash import ascii_hash

class HashFunction:
    def __init__(self, hash_algo: str):
        self.hash_algo = hash_algo
        if hash_algo in hashlib.algorithms_available:
            self.hash_func = getattr(hashlib, hash_algo)
        elif hash_algo == "ascii":
            self.hash_func = ascii_hash
        else:
            raise ValueError(f"{hash_algo} is not available algorithm")

    def __call__(self, passwd: str) -> str:
        if self.hash_algo == "ascii":
            return self.hash_func(passwd)
        return self.hash_func(passwd.encode()).hexdigest()

