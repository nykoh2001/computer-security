from sys import stdin
from collections import defaultdict

from md5_hasher import Md5Hasher


class MaliciousChecker:
    def __init__(self):
        self.virus_names_path = "/Users/nykoh/git/security/vaccine/virus_names.txt"
        self.virus_db_path = "/Users/nykoh/kali/computer_security_6/virus_samples/virus.db"
        self.virus_samples_path = "/Users/nykoh/kali/computer_security_6/virus_samples/"

        self.virus_names = self.read_virus_names()
        self.virus_hashes = self.check_virus_db()

    def check_virus_db(self) -> defaultdict:
        with open(self.virus_db_path, "r") as f:
            virus_hash = f.readlines()

        virus_hashes = defaultdict(str)
        for vh in virus_hash:
            # vh[0] == virus name, vh[1] == virus hash
            v_name, v_hash = vh.split(":")
            virus_hashes[v_name] = v_hash

        return virus_hashes

    def read_virus_names(self) -> list:
        with open(self.virus_names_path, "r") as f:
            virus_names = f.read().splitlines()
        return virus_names

    def compare_md5(self, virus_name: str) -> bool:
        Md5Hasher.initialize()
        target_file_hash = Md5Hasher.hash(self.virus_samples_path + virus_name).rstrip()
        virus_hash = self.virus_hashes.get(virus_name).rstrip()

        if virus_hash == target_file_hash:
            print("Target Hash:", target_file_hash)
            print("Virus Hash:", virus_hash)
            return True
        return False

    def check_malicious(self) -> None:
        virus_name = stdin.readline().rstrip()
        if virus_name not in self.virus_names:
            raise ValueError(f"Virus name '{virus_name}' is not valid.")
        if self.compare_md5(virus_name):
            print(f"{virus_name} is malicious.")
        else:
            print(f"{virus_name} is safe.")


if __name__ == '__main__':
    mc = MaliciousChecker()
    mc.check_malicious()
