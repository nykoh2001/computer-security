import hashlib


class HashFunction:
    def __init__(self, hash_algo: str):
        if hash_algo in hashlib.algorithms_available:
            self.hash_func = getattr(hashlib, hash_algo)
        else:
            raise ValueError(f"{hash_algo} is not available algorithm")

    def __call__(self, passwd: str) -> str:
        return self.hash_func(passwd.encode()).hexdigest()

