import string
import random
import sys


class PasswordGenerator:
    @classmethod
    def create_password(cls, _length: int, _type: int) -> str:
        if _type == 1:
            letter_set = string.digits
        elif _type == 2:
            letter_set = string.ascii_letters
        elif _type == 3:
            letter_set = string.digits + string.ascii_letters
        elif _type == 4:
            letter_set = string.digits + string.ascii_letters + string.punctuation
        else:
            raise ValueError("Invalid type number")

        random_passwd = "".join(random.sample(letter_set, _length))
        print("password:", random_passwd)
        return random_passwd
