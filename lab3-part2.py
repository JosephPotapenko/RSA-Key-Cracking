#I wrote my code to be very verbose and to state every new data point. Helps me keep track of everything. Struggled on lab 2 because I had a lot of data flying around without always seeing what they all were and what I was doing with it.  

#!/usr/bin/python3
from prime import *
import math, sympy

def main():
    print("")

    #given
    C = 1315578006529763640141359009929019255795
    public_key = (3039956819131923800469303260782717053853, 65537)
    n, e = public_key

    print("public key:		", n, ",", e)
    print("ciphertext:		", C)
    print("")

    #factor n into p and q
    prime = sympy.primefactors(n)
    p, q = prime[0], prime[1]
    print("p:			", p)
    print("q: 			", q)
    print("")

    #find lambda(n)
    lm = math.lcm(p - 1, q - 1)

    #find d
    d = modinv(e, lm)
    print("lambda(n):		", lm)
    print("d:			", d)
    print("")

    #decrypt
    M = dcipher(C,d,n)
    print("decrypted int:		", M)

    #int to bytes
    try:
        msg = M.to_bytes((M.bit_length() + 7) // 8)
    except OverflowError:
        msg = b"(decryption failed)"
    print("decrypted message: 	", msg)
    print("")


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m

def cipher(m,e,n):
    i = int.from_bytes(m)
    return pow(i,e,n)

def dcipher(c,d,n):
    return pow(c,d,n)


if __name__ == "__main__":
    main()
