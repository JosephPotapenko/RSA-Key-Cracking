#!/usr/bin/python3
# Retrieved from: http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)?oldid=17104

import random, sys

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def miller_rabin(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

def test_num(num):
    n = int(num)
    return (miller_rabin(n) and "PRIME" or "COMPOSITE")

def gen_prime(nbits):
        while True:
            p = random.getrandbits(nbits)
            p |= 2**nbits | 1
            if miller_rabin(p):
                return p

def main():
    if sys.argv[1] == "test":
        print(test_num(sys.argv[2]))
    elif sys.argv[1] == "genprime":
        print(gen_prime(int(sys.argv[2])))

if __name__ == "__main__":
    main()
