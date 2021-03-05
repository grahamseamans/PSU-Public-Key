# pyright: reportUnusedFunction=false
import secrets
from utility import get_2_generator_prime


class public_key_crypto:
    def __init__(self):
        self.e1 = 2
        self.e2 = 0
        self.p = 0
        self.d = 0
        self.pub_file = "./pubkey.txt"
        self.pri_file = "./prikey.txt"

    """
    def get_private_key(self):
        return self.p, self.e1, self.d

    def get_public_key(self):
        return self.p, self.e1, self.e2
    """

    def make_keys(self):
        self.p = get_2_generator_prime()
        self.d = secrets.randbelow(self.p - 1)
        self.e2 = pow(2, self.d, self.p)
        self.write_keys()

    def read_keys(self):
        with open(self.pri_file, "r") as f:
            self.p, self.e1, self.d = self.parse_keyfile(f)
        with open(self.pub_file, "r") as f:
            self.p, self.e1, self.e2 = self.parse_keyfile(f)

    def parse_keyfile(self, f):
        assert f
        keys = f.readline().split()
        keys = [int(i) for i in keys]
        return keys

    def write_keys(self):
        with open(self.pri_file, "w") as f:
            f.write(str(self.p) + " " + str(self.e1) + " " + str(self.d))
        with open(self.pub_file, "w") as f:
            f.write(str(self.p) + " " + str(self.e1) + " " + str(self.e2))

    def encrypt(self, plain):
        r = secrets.randbelow(self.p)
        C1 = pow(self.e1, r, self.p)
        C2 = ((plain % self.p) * pow(self.e2, r, self.p)) % self.p
        return C1, C2

    def decrypt(self, C1, C2):
        plain = ((C2 % self.p) * pow(C1, self.p - 1 - self.d, self.p)) % self.p
        return plain


if __name__ == "__main__":
    for _ in range(10):
        p = get_2_generator_prime()
        bin_str = bin(p)[2:]
        print(p, bin_str, len(bin_str))

    for _ in range(1000):
        a = secrets.randbelow(100)
        b = secrets.randbelow(100)
        c = secrets.randbelow(100)
        d = secrets.randbelow(100) + 1
        assert (a * b ** c) % d == ((a % d) * pow(b, c, d)) % d
