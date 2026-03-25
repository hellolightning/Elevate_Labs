# 🔐 Secure File Storage System (AES via Fernet)

## 💡 Overview
A lightweight CLI and GUI-based tool to encrypt and decrypt files locally using a password-derived key with PBKDF2HMAC and Fernet (AES-128 + HMAC). This project demonstrates practical file security through authenticated encryption and key derivation — ideal for internship or cybersecurity portfolio submission.

## 📂 Files
File	Description
secure_storage.py	Main script (CLI for encryption & decryption)
secure_storage_gui.py	Tkinter GUI for easy file encryption/decryption
requirements.txt	Python dependencies
sample.txt	Example plaintext file
salt.bin	Example salt file (auto-generated when first run)
report.pdf	professional project report
README.md	Project documentation

## ⚙️ Quick Setup
Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
Generate a salt (only once) or let the tool generate it automatically:

python secure_storage.py genkey --password "YourPass123!" --salt-file salt.bin --out key.bin
Encrypt a file:

python secure_storage.py encrypt --password "YourPass123!" --salt-file salt.bin --in sample.txt --out sample.txt.enc
Decrypt the file:

python secure_storage.py decrypt --password "YourPass123!" --salt-file salt.bin --in sample.txt.enc --out sample_decrypted.txt

## 🖥️ GUI Mode
To use the Graphical Interface, simply run:

python secure_storage_gui.py
You can browse, encrypt, and decrypt files easily without using the command line.

## 🧠 Notes
Keep your salt.bin safe — it's required to regenerate the same key.
Passwords are never stored; keys are derived securely using PBKDF2HMAC.
This project is educational, secure, and suitable for internship or job submissions in cybersecurity and data protection.
