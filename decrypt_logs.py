# decrypt_logs.py
# Tool to decrypt logs from encrypted_log.txt

from cryptography.fernet import Fernet
import base64
import os

KEY_PATH = "secret.key"
LOG_FILE = "encrypted_log.txt"

# Load the Fernet key
def load_key():
    with open(KEY_PATH, "rb") as f:
        return f.read()

# Decrypt each base64-encoded encrypted line
def decrypt_logs():
    if not os.path.exists(LOG_FILE):
        print("[!] No log file found.")
        return

    key = load_key()
    fernet = Fernet(key)

    print("\n[+] Decrypted Logs:\n")
    with open(LOG_FILE, "rb") as f:
        for line in f:
            try:
                encrypted = base64.b64decode(line.strip())
                decrypted = fernet.decrypt(encrypted).decode()
                print(decrypted, end="")
            except Exception as e:
                print("[!] Failed to decrypt a line:", e)

if __name__ == "__main__":
    decrypt_logs()
