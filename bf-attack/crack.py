import sys
import time

from bruteforce_attacker import BruteForceAttacker
from password_generator import PasswordGenerator
from hash_function import HashFunction


def main(hash_algo) -> None:
    print("패스워드 길이를 입력해주세요: ", end="")
    length = int(input())

    print("패스워드가 이루어지는 형태 (1.숫자, 2.알파벳, 3.숫자 + 알파벳, 4.숫자 + 알파벳 + 특수문자)를 입력하세요: ", end="")
    _type = int(input())

    hash_func = HashFunction(hash_algo)

    password = PasswordGenerator.create_password(length, _type)
    password_hash = hash_func(password)
    print("password hash:", password_hash)

    attacker = BruteForceAttacker(_type, length, hash_algo)
    attacker.attack(password_hash)


if __name__ == "__main__":
    main(sys.argv[1])
