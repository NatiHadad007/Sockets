import socket
import glob
import os
import shutil
import subprocess

del_cmd = r"DELETE C:\Cyber\blabla.txt"

def check_client_request(cmd):
    files_list = glob.glob(r"C:\Cyber\*.*")
    if cmd == del_cmd:
        for files in files_list:
            os.remove(files)
        print("delete files")
    elif cmd == "COPY":
            shutil.copy(r"C:\Cyber\1.txt", r"C:\Cyber\2.txt")
            print("C:\Cyber\1.txt copy to C:\Cyber\2.txt")
    elif cmd == "EXECUTE":
            subprocess.call(r'C:\Windows\system32\notepad.exe')
            print("open notepad.exe")
    else:
        print("not deleted")
        client_socket.close()



server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen()
print("Server is up and running")

while True:
    print("Waiting for client to connect...")
    client_socket, client_address = server_socket.accept()

    data = client_socket.recv(1024).decode()
    command = client_socket.recv(1024).decode()

    if data and command:
        check_client_request(command)
        print("Client sent: " + data)
        reply = "Hello " + data + " " +  command
        client_socket.send(reply.encode())
    else:
        print("No data received.")

    client_socket.close()
    print("Client disconnected.\n")
