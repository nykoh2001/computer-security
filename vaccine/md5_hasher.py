import hashlib


class Md5Hasher:
    _hasher = None

    # Singleton MD5 Hasher
    @classmethod
    def initialize(cls):
        if cls._hasher is None:
            cls._hasher = hashlib.md5()

    @classmethod
    def get_instance(cls):
        cls.initialize()
        return cls._hasher

    @classmethod
    def hash(cls, filepath: str) -> str:
        with open(filepath, "rb") as f:
            data = f.read()
            cls._hasher.update(data)
            return cls._hasher.hexdigest()
