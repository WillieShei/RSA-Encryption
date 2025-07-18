import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    # Extended Euclidean Algorithm
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2, x1 = x1, x
        d, y1 = y1, y

    return d + phi if temp_phi == 1 else None

def generate_keys(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be the same.")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # Common choice for e
    if gcd(e, phi) != 1:
        # Find a new e manually
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = mod_inverse(e, phi)
    if d is None:
        raise ValueError("Failed to find modular inverse of e.")

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

def main():
    print("=== RSA Cryptography App ===")

    try:
        p = int(input("Enter a prime number (p): "))
        q = int(input("Enter another prime number (q): "))
        public_key, private_key = generate_keys(p, q)
    except ValueError as ve:
        print(f"Error: {ve}")
        return

    print(f"\nPublic Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")

    message = input("\nEnter a message to encrypt: ")
    encrypted = encrypt(public_key, message)
    print("Encrypted message:", encrypted)

    decrypted = decrypt(private_key, encrypted)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
