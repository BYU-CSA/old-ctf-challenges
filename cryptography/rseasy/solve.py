from sympy import nextprime


# return the integer square root of n
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def readInput():
    """
    read n, e, and ciphertext from file
    """
    with open('output.txt', 'r') as f:
        n = int(f.readline().strip().split(" ")[1])
        e = int(f.readline().strip().split(" ")[1])
        ciphertext = int(f.readline().strip().split(" ")[1])
        return n, e, ciphertext


def main():
    n, e, ciphertext = readInput()
    p = nextprime(isqrt(n))
    q = n // p
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    message = pow(ciphertext, d, n)
    print("message:", message.to_bytes(
        (message.bit_length() + 7) // 8, "big").decode())


if __name__ == "__main__":
    main()
