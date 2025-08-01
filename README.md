# 🔓 Simple Hash Cracker

This is a basic Python script that attempts to crack hashed strings using a wordlist.  
It supports `MD5`, `SHA1`, and `SHA256` hashes.

---

## 💡 What it does

You give it:
- A hash to crack
- The hash algorithm used (`md5`, `sha1`, or `sha256`)
- A path to a wordlist (like `rockyou.txt`)

It will loop through every word in the wordlist, hash it using the selected algorithm, and compare it to your input hash. If there's a match, it prints the original word.

---

## 🛠️ Requirements

- Python 3.X.X

---

## 📦 Example usage

```bash
$ python hash_cracker.py
=== Simple Hash Cracker ===
Enter the hash: 5d41402abc4b2a76b9719d911017c592
Hash type (md5 / sha1 / sha256): md5
Path to wordlist (e.g., rockyou.txt): wordlist.txt
[+] Hash cracked in 0.12 ms → 'hello'
```
