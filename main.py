import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import os
import sys

def clear_screen():
    # للأوامر الويندوز
    if os.name == 'nt':
        os.system('cls')
    # للأنظمة المشابهة ليونكس (لينكس، ماك)
    else:
        os.system('clear')

def get_key(password):
    return hashlib.md5(password.encode()).digest()

def encrypt_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    
    if not file_path:
        return
    
    password = input("Enter Password: ")
    key = get_key(password)
    
    output_file = file_path + '.cccpe'
    iv = os.urandom(16)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    
    ciphertext = iv + cipher.encrypt(pad(plaintext, AES.block_size))
    
    with open(output_file, 'wb') as f:
        f.write(ciphertext)
    
    print(f"File encrypted successfully: {output_file}")
    input("\nPress Enter to return to main menu...")

def decrypt_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("CCCPE Files", "*.cccpe")])
    
    if not file_path:
        return
    
    if not file_path.endswith('.cccpe'):
        print("Invalid file format!")
        return
    
    password = input("Enter Password: ")
    key = get_key(password)
    
    with open(file_path, 'rb') as f:
        ciphertext = f.read()
    
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    try:
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    except ValueError:
        print("Incorrect password or corrupted file!")
        input("\nPress Enter to return to main menu...")
        return
    
    output_file = file_path[:-6]
    
    with open(output_file, 'wb') as f:
        f.write(plaintext)
    
    print(f"File decrypted successfully: {output_file}")
    input("\nPress Enter to return to main menu...")

def main_menu():
    while True:
        clear_screen()
        print("╔══════════════════════════╗")
        print("║     File Cipher - AES    ║")
        print("╠══════════════════════════╣")
        print("║ 1. Encrypt File          ║")
        print("║ 2. Decrypt File          ║")
        print("║ 3. Exit                  ║")
        print("╚══════════════════════════╝")
        
        choice = input("\n>> Select option (1-3): ").strip()
        
        if choice == '1':
            encrypt_file()
        elif choice == '2':
            decrypt_file()
        elif choice == '3':
            clear_screen()
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")
            input("\nPress Enter to try again...")

if __name__ == "__main__":
    main_menu()
