"""
Secure File Storage System (AES via Fernet) - CLI + Library
This file contains:
- Well-documented functions for key derivation, salt generation, encryption, and decryption.
- A small CLI wrapper (same commands as before).
This version is commented and suitable for educational submission.
"""

import argparse
import base64
import os
import json
from typing import Optional
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend

def derive_key_from_password(password: str, salt: bytes, iterations: int = 390000) -> bytes:
    """
    Derive a 32-byte URL-safe base64-encoded key from a password using PBKDF2HMAC.
    - password: the user's passphrase (str)
    - salt: 16-byte salt (bytes)
    - iterations: PBKDF2 iterations (int) - higher is slower but more resistant to brute force
    Returns:
    - key (bytes) that can be used with Fernet.
    """
    # Create the key-derivation function (KDF) object with SHA256
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,            # 32 bytes = 256 bits
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    # Derive the raw key bytes and encode to URL-safe base64 (required by Fernet)
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def generate_salt(salt_file: str) -> None:
    """
    Generate a 16-byte random salt and write it to salt_file.
    Salt is not secret but must be preserved to derive the same key later.
    """
    salt = os.urandom(16)
    with open(salt_file, "wb") as f:
        f.write(salt)
    print(f"[+] Salt saved to {salt_file}")

def gen_key(password: str, salt_file: str, out_file: Optional[str] = None) -> None:
    """
    Generate a derived key from password and given salt_file.
    If salt_file does not exist, a new salt will be generated.
    If out_file is provided, save the derived key (base64) to that file.
    """
    if not os.path.exists(salt_file):
        # Automatically create salt if missing to simplify usage
        print(f"[!] Salt file {salt_file} not found. Generating a new salt.")
        generate_salt(salt_file)
    with open(salt_file, "rb") as f:
        salt = f.read()
    key = derive_key_from_password(password, salt)
    if out_file:
        with open(out_file, "wb") as f:
            f.write(key)
        print(f"[+] Key saved to {out_file} (base64 urlsafe)")
    else:
        # Print key to stdout (base64)
        print(key.decode())

def encrypt_file(password: str, salt_file: str, in_file: str, out_file: Optional[str] = None) -> None:
    """
    Encrypt a file using a password-derived key.
    - password: user password
    - salt_file: path to salt file used for key derivation
    - in_file: input plaintext file to encrypt
    - out_file: output encrypted filename (.enc by default)
    This function also writes a small .meta JSON file next to the encrypted file
    containing original filename and size for user convenience.
    """
    if not os.path.exists(in_file):
        raise FileNotFoundError(in_file)
    if not os.path.exists(salt_file):
        # Salt missing -> cannot derive key
        raise FileNotFoundError(f"Salt file not found: {salt_file}")
    with open(salt_file, "rb") as f:
        salt = f.read()
    # Derive the key and create a Fernet object (AEAD)
    key = derive_key_from_password(password, salt)
    fernet = Fernet(key)
    with open(in_file, "rb") as f:
        data = f.read()
    # Encrypt the data; Fernet includes a timestamp and HMAC for integrity
    token = fernet.encrypt(data)
    if not out_file:
        out_file = in_file + ".enc"
    with open(out_file, "wb") as f:
        f.write(token)
    # Save metadata for easier decryption and verification
    meta = {
        "orig_name": os.path.basename(in_file),
        "orig_size": len(data)
    }
    with open(out_file + ".meta", "w") as f:
        json.dump(meta, f)
    print(f"[+] Encrypted {in_file} -> {out_file}")
    print(f"[+] Metadata saved to {out_file}.meta")

def decrypt_file(password: str, salt_file: str, in_file: str, out_file: Optional[str] = None) -> None:
    """
    Decrypt an encrypted file using the same password and salt.
    - password: user password
    - salt_file: path to salt file
    - in_file: input encrypted file (the token produced by Fernet)
    - out_file: optional output filename to store decrypted bytes
    """
    if not os.path.exists(in_file):
        raise FileNotFoundError(in_file)
    if not os.path.exists(salt_file):
        raise FileNotFoundError(f"Salt file not found: {salt_file}")
    with open(salt_file, "rb") as f:
        salt = f.read()
    key = derive_key_from_password(password, salt)
    fernet = Fernet(key)
    with open(in_file, "rb") as f:
        token = f.read()
    try:
        data = fernet.decrypt(token)
    except Exception as e:
        # Decryption failed: likely wrong password or tampered file
        print("[!] Decryption failed. Wrong password or corrupted file.")
        raise
    if not out_file:
        # Attempt to read metadata to recover original filename
        meta_file = in_file + ".meta"
        if os.path.exists(meta_file):
            try:
                with open(meta_file, "r") as mf:
                    import json
                    meta = json.load(mf)
                    out_file = "decrypted_" + meta.get("orig_name", "output.bin")
            except Exception:
                out_file = "decrypted_output.bin"
        else:
            out_file = "decrypted_output.bin"
    with open(out_file, "wb") as f:
        f.write(data)
    print(f"[+] Decrypted {in_file} -> {out_file}")

# --- CLI wrapper for convenience (same interface as before) ---
def main():
    parser = argparse.ArgumentParser(description="Secure File Storage System (AES via Fernet)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_gen = sub.add_parser("genkey", help="Generate derived key file from password and salt")
    p_gen.add_argument("--password", required=True)
    p_gen.add_argument("--salt-file", required=True)
    p_gen.add_argument("--out", required=False)

    p_encrypt = sub.add_parser("encrypt", help="Encrypt a file")
    p_encrypt.add_argument("--password", required=True)
    p_encrypt.add_argument("--salt-file", required=True)
    p_encrypt.add_argument("--in", dest="in_file", required=True)
    p_encrypt.add_argument("--out", dest="out_file", required=False)

    p_decrypt = sub.add_parser("decrypt", help="Decrypt a file")
    p_decrypt.add_argument("--password", required=True)
    p_decrypt.add_argument("--salt-file", required=True)
    p_decrypt.add_argument("--in", dest="in_file", required=True)
    p_decrypt.add_argument("--out", dest="out_file", required=False)

    args = parser.parse_args()
    if args.cmd == "genkey":
        gen_key(args.password, args.salt_file, args.out)
    elif args.cmd == "encrypt":
        encrypt_file(args.password, args.salt_file, args.in_file, args.out_file)
    elif args.cmd == "decrypt":
        decrypt_file(args.password, args.salt_file, args.in_file, args.out_file)

if __name__ == "__main__":
    main()
