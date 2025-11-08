#I used math.lcm, which requires python 3.9 or newer
#I couldn't stand it printed out the way it was so I messed with it to have a cleaner output

#!/usr/bin/python3
from prime import *
import math, random, sys

def main():
 
    print("")

    public,private = make_key(int(sys.argv[1]))

    #public key = (n,e)
    print(f"public key is:  ({public[0]},{public[1]})")

    #private key = (n,d)
    print(f"private key is: ({private[0]},{private[1]})")
    #message to encrypt
    msg = b'test,message'
 
    print("")

    print("message:       ", msg)
    print("int from bytes:", int.from_bytes(msg))

 
    print("")


    #cipher with public key
    x = cipher(msg,public[1],public[0])
    print("ciphered:      ", x)

    #decipher with private key
    y = dcipher(x, private[1], private[0])
    print("deciphered:    ", y.to_bytes(len(msg)))
    
    print("")

    #encrypt with private key 
    ciph = cipher_d(msg, private[1], private[0])
    print("encrypted:     ", ciph)

    #decrypt with public key
    dciph = dcipher(ciph, public[1], public[0])
    print("decrypted:     ", dciph.to_bytes(len(msg)))
    
    print("")


def cipher(m,e,n):
    i = int.from_bytes(m)
    return pow(i,e,n)

def dcipher(c,d,n):
    return pow(c,d,n)

#technically redundant, but it'll help me remember when I look back at this
def cipher_d(m, d, n):
    i = int.from_bytes(m)
    return pow(i, d, n)

"""
FINISH THIS FUNCTION
You'll need a function from prime.py
"""
def make_key(bit_len):
    # compute n and d
    # (n,e) is your public key
    # (n,d) is your private key
    # use 65537 as e
    
    p = gen_prime(bit_len)
    q = gen_prime(bit_len)
    while q == p:
        q = gen_prime(bit_len)
    n = p * q
    lm = math.lcm(p-1, q-1)
    e = 65537
    d = modinv(e,lm)
    
    return((n,e),(n,d))

#found this code somewhere (Greatest common denominator)
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

"""
function to find modular multiplicative inverse in RSA
must give e and totient (in our case lambda(n) = lm)
stole this code too :)
"""
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

if __name__ == "__main__":
    main()
