
---


#  RSA Cryptography App

An interactive Python application that demonstrates the fundamentals of RSA encryption and decryption. Users input their own prime numbers `p` and `q` to generate RSA keys, encrypt plaintext messages, and decrypt them using the private key — all from the terminal.

---

##  Features

-  Manual input of prime numbers `p` and `q`
-  RSA key pair generation (public and private)
-  Encrypts plaintext into cipher text
-  Decrypts cipher text into readable text
-  Input validation and basic error handling
-  Beginner-friendly, educational design

---

##  Concepts Covered

- Prime number theory  
- Modular arithmetic  
- Euler’s Totient Function  
- Public-key cryptography (asymmetric encryption)  
- Greatest Common Divisor (GCD)  
- Modular Inverse (Extended Euclidean Algorithm)  

---

##  Technologies Used

-  Python 3 (no third-party libraries required)

---

##  Getting Started

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/rsa_encryption.git
   cd rsa_encryption/src
   

2. **Run the application:**

   ```
   python rsa_encryption.py
   ```

3. **Follow the prompts:**

   * Enter two distinct prime numbers
   * View your public/private keys
   * Enter a message to encrypt
   * View encrypted & decrypted output

---

##  Example Run

```
Enter a prime number (p): 61
Enter another prime number (q): 53
Public key: (17, 3233)
Private key: (2753, 3233)
Enter a message to encrypt: hello
Encrypted message: [2038, 131, 1666, 1666, 2202]
Decrypted message: hello
```

---

##  Use Cases

This project is great for:

* Cybersecurity & computer science students
* Educators teaching RSA or encryption basics
* Developers who want a simple working example of RSA


##  Contributing

Pull requests are welcome! Feel free to fork the repo and open a PR with improvements.

---


