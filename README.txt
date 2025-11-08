Lab3: RSA encryption/cracking


Files:

lab3-part1.py – Generates RSA keys and tests encryption and decryption.
lab3-part2.py – Cracks an RSA ciphertext by finding the prime factors and calculating d, and doing the mod inverse.
lab3-part3.py – Tests, times, and creates a graph for RSA key cracking with increasing bits for prime numbers.
prime.py – lots of useful functions- some of which I added into the code itself- some of which I didn't.

Requirements:

Python 3.9+
Modules: math, random, sympy, matplotlib 




Part 1 (lab3-part1.py):

Run from the terminal with:
python lab3-part1.py <bit_length>
Example: python lab3-part1.py 64
It basically encrypts and decrypts a sample message provided. Cool stuff. 




Part 2 (lab3-part2.py):

Run from the terminal with:
python lab3-part2.py
This code is static. only works with the info provided in the assignment. Takes in the public key, does the whole process described in the pdf, and decrypts the message.
I printed out every step because I wanted to make sure I didn't get lost/confused. Plus, if I look back, this will be great. 



Part 3 (lab3-part3.py):

Run from the terminal with:
python lab3-part3.py
This code is also somewhat static. This code tests how long it takes to break RSA keys of different bit sizes.
It factors the numbers, times each run, and prints the average time for each size.
Higher bit sizes take much longer to crack. If you run this program to test it, expect to wait 5 hours. 
If you'd like to shorten the wait time, change the following:
bit_sizes = [64, 74, 84, 94, 104]

to:
bit_sizes = [64, 74]

This will help tremendously while showing it functions properly. I provided the output of my code in the pdf and as a file if you want to see what it looks like.




prime.py:

Contains helper functions that gets used in other programs. Didn't change this from original.

