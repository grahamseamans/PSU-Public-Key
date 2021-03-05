import random
import secrets


def get_2_generator_prime():
    keysize = 32
    p = 4  # some not prime number
    while not is_prime(p):
        q = rand_bits_max_filled(keysize)
        while q % 15 != 5:
            q = rand_bits_max_filled(keysize)
        p = 2 * q + 1
    return p


def is_prime(n):
    """
    https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n != int(n):
        return False
    n = int(n)
    # Miller-Rabin test for prime
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert 2 ** s * d == n - 1

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for _ in range(8):  # number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True


def rand_bits_max_filled(bits):
    a = secrets.randbits(bits)
    a = a | 1 << bits - 1
    return a


if __name__ == "__main__":
    print(is_prime(1))
    print(is_prime(10))
    print(is_prime(7907))
    print(is_prime(7919))

    a = rand_bits_max_filled(8)
    print(a, bin(a))
