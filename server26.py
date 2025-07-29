# please use specific imports
import socket
import glob
import os
import shutil
import subprocess

#this is a global variable, this shoud be named in CAPSLOCK
# Also dont use this variable, if anything create a variable that is that file path and a dictionary of options to preform on it
del_cmd = r"DELETE C:\Cyber\blabla.txt"

# please split functionalities in this function into fregments, each function should only preform one task, this function preforms several
def check_client_request(cmd):
    #add a docstring

    #u already import os, theres a way to do it using os, use it, and find a better name then files lis (what files?)
    files_list = glob.glob(r"C:\Cyber\*.*")

    # come back to me with a solution of what will u do if u had 1000 cases to take care of, would you create 1000 elif?
    # according to the answer to what i said fix this accordingly
    if cmd == del_cmd:
        # please look up list comprehension python
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


# why is this all outside a function? create a main function and an if __name__ thingy
# apply what i said in the client side about this parts
# atleast in here you named it fine <3
# maybe conside creating an init method here for this bunch  of lines
server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen()

# this is a server side, log it into a file not the terminal, this is a better approach
print("Server is up and running")

#this is not a good hobby, there should be a stop signal and not while True
#also handle erros inide this while loop
while True:
    # this is nice u printed u are waiting, please create a follow up print that says the client connected
    print("Waiting for client to connect...")
    client_socket, client_address = server_socket.accept()

    # so you recieve 2 packets for 1 action? nah do it in one using a couple or somthing
    data = client_socket.recv(1024).decode()
    command = client_socket.recv(1024).decode()

    # this only checks if there is data and command sent not if they are valid
    if data and command:
        # this is a nice way to do what u did, i like
        check_client_request(command)

        #learn about format strings f"", better practice
        print("Client sent: " + data)

        # please find a better way to construct a string
        reply = "Hello " + data + " " +  command
        client_socket.send(reply.encode())
    else:
        # this doesnt happen if no data is recieved it happens if data or a command is recieved, either handle what happens each time one isnt recieved or change the text
        print("No data received.")
    # i like how tell after but not before, fix it its sarcasm
    # also what happens if the loop crashed for some reason before it reaches this line? also why do you open a new socket and close it each loop iteration? 
    # why not make it once and check if the client closed it?
    client_socket.close()
    # damn nice newline, use it more often
    print("Client disconnected.\n")
