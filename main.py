import hashlib
import time

def crack_hash(target_hash, hash_type, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            start = time.time()
            for word in file:
                word = word.strip()
                if hash_type == "md5":
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == "sha1":
                    hashed_word = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == "sha256":
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                else:
                    print("[-] Unsupported hash type.")
                    return

                if hashed_word == target_hash.lower():
                    end = time.time()
                    print(f"[+] Hash cracked in {end - start} ms → '{word}'")
                    return
        end = time.time()
        print(f"[-] Hash not found in wordlist. (Search took {end - start} ms)")
    except FileNotFoundError:
        print("[-] Wordlist file not found.")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    print("=== Simple Hash Cracker ===")
    target_hash = input("Enter the hash: ").strip()
    hash_type = input("Hash type (md5 / sha1 / sha256): ").lower().strip()
    wordlist_path = input("Path to wordlist (e.g., rockyou.txt): ").strip()
    
    crack_hash(target_hash, hash_type, wordlist_path)
