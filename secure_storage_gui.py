"""
Secure File Storage - Tkinter GUI
Simple GUI wrapper around secure_storage functions to:
- Select salt file, select input file
- Enter password
- Encrypt / Decrypt with buttons
This file can be run directly: python secure_storage_gui.py
"""
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import threading
from secure_storage import encrypt_file, decrypt_file, generate_salt

# Helper to run encryption/decryption in a separate thread to keep UI responsive
def run_in_thread(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs, daemon=True).start()
    return wrapper

class SecureStorageGUI:
    def __init__(self, root):
        self.root = root
        root.title("Secure File Storage - GUI")
        root.geometry("600x300")
        # Password entry
        tk.Label(root, text="Password:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(root, textvariable=self.password_var, show="*")
        self.password_entry.grid(row=0, column=1, columnspan=3, sticky="we", padx=5, pady=5)

        # Salt file selection
        tk.Label(root, text="Salt file:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.salt_var = tk.StringVar(value="salt.bin")
        tk.Entry(root, textvariable=self.salt_var).grid(row=1, column=1, sticky="we", padx=5, pady=5)
        tk.Button(root, text="Browse", command=self.browse_salt).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(root, text="Generate Salt", command=self.generate_salt_file).grid(row=1, column=3, padx=5, pady=5)

        # Input file selection
        tk.Label(root, text="Input file:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.input_var = tk.StringVar()
        tk.Entry(root, textvariable=self.input_var).grid(row=2, column=1, sticky="we", padx=5, pady=5)
        tk.Button(root, text="Browse", command=self.browse_input).grid(row=2, column=2, padx=5, pady=5)

        # Output filename (optional)
        tk.Label(root, text="Output file (optional):").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.output_var = tk.StringVar()
        tk.Entry(root, textvariable=self.output_var).grid(row=3, column=1, sticky="we", padx=5, pady=5)

        # Buttons
        tk.Button(root, text="Encrypt", command=self.encrypt).grid(row=4, column=1, padx=5, pady=15)
        tk.Button(root, text="Decrypt", command=self.decrypt).grid(row=4, column=2, padx=5, pady=15)

        # Status box
        self.status = tk.Text(root, height=6)
        self.status.grid(row=5, column=0, columnspan=4, sticky="we", padx=5, pady=5)
        # make columns resize nicely
        root.grid_columnconfigure(1, weight=1)

    def browse_salt(self):
        path = filedialog.askopenfilename(title="Select salt file")
        if path:
            self.salt_var.set(path)

    def browse_input(self):
        path = filedialog.askopenfilename(title="Select input file")
        if path:
            self.input_var.set(path)

    def append_status(self, text):
        self.status.insert("end", text + "\n")
        self.status.see("end")

    def generate_salt_file(self):
        path = filedialog.asksaveasfilename(title="Save salt as", defaultextension=".bin", initialfile="salt.bin")
        if path:
            try:
                generate_salt(path)
                messagebox.showinfo("Success", f"Salt generated: {path}")
                self.salt_var.set(path)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    @run_in_thread
    def encrypt(self):
        pwd = self.password_var.get()
        salt = self.salt_var.get()
        infile = self.input_var.get()
        outfile = self.output_var.get() or None
        if not pwd or not salt or not infile:
            messagebox.showwarning("Missing fields", "Please provide password, salt file, and input file.")
            return
        try:
            encrypt_file(pwd, salt, infile, outfile)
            self.append_status(f"[+] Encrypted {infile}")
            messagebox.showinfo("Done", "Encryption complete.")
        except Exception as e:
            self.append_status(f"[!] Encryption error: {e}")
            messagebox.showerror("Error", str(e))

    @run_in_thread
    def decrypt(self):
        pwd = self.password_var.get()
        salt = self.salt_var.get()
        infile = self.input_var.get()
        outfile = self.output_var.get() or None
        if not pwd or not salt or not infile:
            messagebox.showwarning("Missing fields", "Please provide password, salt file, and input file.")
            return
        try:
            decrypt_file(pwd, salt, infile, outfile)
            self.append_status(f"[+] Decrypted {infile}")
            messagebox.showinfo("Done", "Decryption complete.")
        except Exception as e:
            self.append_status(f"[!] Decryption error: {e}")
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = SecureStorageGUI(root)
    root.mainloop()
