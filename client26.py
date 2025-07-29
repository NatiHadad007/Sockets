# specific imports please not general ones, its done like: from socket import ...
# bonus points if you tell me why is it better what i said
import socket


#dont put all the code in main!!!! create a function and call it from main its more correct | i would even rather you do it
#in a class so u could learn OOP programing (look it up if u dont know the term), also give it a proper name that describes what it does
def main():
    #A function always no matter what you do should include a docstring which is a string like this:
    # description:
    # param 1 something: #this is an arguemnt passed to the function, if theres more add more
    # return: #what does the function return
    
    # name this better, my_x isnt acceptable, even when learning do it the most proffesional way possible, name it something like server_socket
    my_socket = socket.socket()

    # no wild strings from now on! if u want to use a string you create a variable and assign the variable instead of the string directly like:
    # client_hostname: str = "127.0.0.1"  # find out what was that - ": str" i did there and use that, same goes for port number
    # look up in the internet a way to validate an IP address using a lib
    # bonus points if the user on runtime provides arguemnts port and hostname that will be used there
    my_socket.connect(("127.0.0.1", 8820))

    # always after an input validate the content and handle errors, btw always finish a printed string with a \n
    # find a better name
    name = input("What is your name? ")

    #same for here as for the last one
    user_command = input("What is your command? ")

    # please lookup error handeling, i want you to cover errors that might happen for both those lines
    # imma kick you in the butt if you send 2 packets instead of one just coupled with the information
    my_socket.send(name.encode())
    my_socket.send(user_command.encode())

    # what is that 1024 stands for
    data = my_socket.recv(1024).decode()

    #please use f"", its called a strings format, look it up
    print("The server sent " + data)

    # Pro Tip people usually close it twice or make sure its closed by checking state, find out how
    my_socket.close()

# this is a nice habbit good job keep it up, write for me in whatsapp why did you do it, the reason behind this habbit is important
if __name__ == "__main__":
    main()
# that last line is a banger, i like it you should always keep one line empty at the end of the code
