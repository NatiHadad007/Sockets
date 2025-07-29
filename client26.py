import socket


def main():
    my_socket = socket.socket()
    my_socket.connect(("127.0.0.1", 8820))
    name = input("What is your name? ")
    user_command = input("What is your command? ")
    my_socket.send(name.encode())
    my_socket.send(user_command.encode())
    data = my_socket.recv(1024).decode()
    print("The server sent " + data)

    my_socket.close()


if __name__ == "__main__":
    main()
