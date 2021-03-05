from crypt import public_key_crypto
import sys


class driver:
    def __init__(self):
        self.crypt = public_key_crypto()
        self.file_plain = "./plaintext.txt"
        self.file_encrypted = "./ciphertext.txt"

    def make_keys(self):
        self.crypt.make_keys()

    def decrypt(self):
        self.crypt.read_keys()
        with open(self.file_encrypted, "r") as cipher_reader:
            with open(self.file_plain, "w") as plain_writer:
                for line in cipher_reader:
                    C = line.split()
                    C = [int(i) for i in C]
                    plain_number = self.crypt.decrypt(C[0], C[1])
                    plain_block = self.bin_to_ascii(plain_number)
                    plain_writer.write(str(plain_block))

    def encrypt(self):
        self.crypt.read_keys()
        with open(self.file_plain, "r") as p:
            with open(self.file_encrypted, "w") as c:
                p = "".join(p.readlines())
                while p:
                    plain_block = p[:4]
                    p = p[4:]
                    plain_block = self.str_to_int(plain_block)
                    C1, C2 = self.crypt.encrypt(plain_block)
                    c.write(str(C1) + " " + str(C2) + "\n")

    def str_to_int(self, string):
        return int("".join(format(ord(i), "08b") for i in string), 2)

    def bin_to_str(self, binary, lenght):
        string = bin(binary)[2:]
        while len(string) < lenght:
            string = "0" + string
        return string

    def bin_to_ascii(self, binary):
        string = self.bin_to_str(binary, lenght=32)
        out = ""
        while string:
            character = string[:8]
            string = string[8:]
            out += chr(int(character, 2))
        return out


if __name__ == "__main__":
    dri = driver()

    if len(sys.argv) <= 1:
        encrypt_decrypt_keys = input("e for encrypt, d for decrypt, k to make keys: ")
    else:
        encrypt_decrypt_keys = sys.argv[1]

    if encrypt_decrypt_keys == "e":
        dri.encrypt()
    elif encrypt_decrypt_keys == "d":
        dri.decrypt()
    elif encrypt_decrypt_keys == "k":
        dri.make_keys()
    else:
        print("bad input")
