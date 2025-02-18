import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import os
import sys
# مسموج لك العبث بالبرنامج وتخربه وتزبطه على كيفك وخذ راحتك ياشنب .. بس جرب وسو تجارب على راحتك واي سوال راسلني تويتر
# x.com/0xreed 
##################################
def clear_screen(): # ينظف نافذه cmd :)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
##################################
def get_key(password): # علشان ياخذ الباسوورد ويحوله لهاش ام دي فايف ويستخدم الهاش كمفتاح للتشفير :(
    return hashlib.md5(password.encode()).digest()
##################################
def encrypt_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename() # هنا تطلع لك النافذه اللي تختار منها الملف اللي بتشفره
    
    if not file_path: # مابيصير شي اذا ماخترت ملف يعني مايتغير ولا حاجه بالقائمه اذا ماخترت ملف :)
        return
    
    password = input("Enter Password: ") # ادخال الرقم السري
    key = get_key(password)
    
    output_file = file_path + '.0xreed' # الصيغه : يمدي تغيرها بس اذا بتغيرها هنا غيرها بكل مكان بالكود وحط صيغه خاصه لك مو تجلطني وتحط صيغه ملف ام بي ثري مثلا ههه
    iv = os.urandom(16)
    
    cipher = AES.new(key, AES.MODE_CBC, iv) # التشفير
    
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    
    ciphertext = iv + cipher.encrypt(pad(plaintext, AES.block_size))
    
    with open(output_file, 'wb') as f:
        f.write(ciphertext)
    
    print(f"File encrypted successfully: {output_file}") # مبروك صديق تم التشفير ..
    input("\nPress Enter to return to main menu...")

def decrypt_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("0xreed Files", "*.0xreed")]) # هنا يطلع لك نافذه ويعرض لك بس التطبيقات اللي بالصيغه المشفره علشان تختارها وتفكها
    
    if not file_path: # نفس اللي قلناه قبل مدري ليش قاعد اكتب لك هنا بس طفشان
        return
    
    if not file_path.endswith('.0xreed'): # الصيغه مثل ماقلت لك بالفنكشن الاول اذا بتغيره غيره بكل الكود 
        print("Invalid file format!")
        return
    
    password = input("Enter Password: ") # ادخال الرقم السري ..
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
    
    print(f"File decrypted successfully: {output_file}") # مبروك لقد ربحت الجايزه .. اقصد تم فك التشفير
    input("\nPress Enter to return to main menu...")

def main_menu(): # هذا سلمك الله علشان الواجهه شكل التطبيق في سي ام دي والخيارات حقتها
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
            print("Goodbye ...")
            break
        else:
            print("Invalid choice!")
            input("\nPress Enter to try again...")

if __name__ == "__main__":
    main_menu()
