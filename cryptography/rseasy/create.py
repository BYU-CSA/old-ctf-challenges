from sympy import nextprime
from random import randint


# read first line from file
def readFlag():
    with open('flag.txt', 'r') as f:
        return f.readline().strip()


def main():
    size = 4096
    p = nextprime(randint(2**size, 2**(size+1)))
    q = nextprime(p)
    n = p * q
    e = 65537
    print("n:", n)
    print("e:", e)
    flag = readFlag()
    message = int.from_bytes(flag.encode(), "big")
    ciphertext = pow(message, e, n)
    print("ciphertext:", ciphertext)


if __name__ == "__main__":
    main()
