#!/usr/bin/python3
from prime import *
import math, sympy, time, statistics, matplotlib.pyplot as plt

def main():
    print("")
    print("RSA key cracking")
    print("")

    #increment by 10, but when I hit 114, it took like 1/2 hour and nothing happened, so I decided to rewrite it to be more managable. 
    bit_sizes = [64, 74, 84, 94, 104]
    avg_times = []

    #4 tests which is 3-5
    tests = 4
    for bits in bit_sizes:
        print(f"Testing {bits}-bit primes")
        times = []

        for i in range(tests):
            start = time.time()

            p = gen_prime(bits)
            q = gen_prime(bits)
            while q == p:
                q = gen_prime(bits)
            n = p * q

            sympy.primefactors(n)

            end = time.time()
            elapsed = end - start
            times.append(elapsed)
            print(f"   Test {i+1}: {elapsed:.4f} seconds")

        avg = statistics.mean(times)
        avg_times.append(avg)
        print(f"Average for {bits}-bit")
        print(f"Time: {avg:.4f} seconds")
        print("")

    #plot
    plot_points(bit_sizes, avg_times)

    print("")
    print("Experiment complete.")
    print("Plot saved as: rsa_crack_times.png")
    print("")


def plot_points(bit_sizes, avg_times):
    plt.figure(figsize=(8, 5))
    plt.plot(bit_sizes, avg_times, marker='o', linestyle='-', linewidth=2)
    plt.title("RSA Key Cracking Time VS. Bit Size")
    plt.xlabel("bits per prime (key size component)")
    plt.ylabel("avg. time to crack (sec.)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("rsa_crack_times.png")
    plt.show()


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


if __name__ == "__main__":
    main()
