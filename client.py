"""
BashChat Client Script
Author(s): Micah Hauge, ...(feel free to add your name here if you contributed)
Last Updated: 6/22/2016 by Micah Hauge
"""

import socket
import sys


# Testing locally for now. This will be easy to change later though
HOST = 'localhost'

# use specified port if it was given by user, else use port 8000
if sys.argv[1:]:
    PORT = int(sys.argv[1])
else:
    PORT = 9001

# size per message (in bytes) This is plenty for simple text messages.
SIZE = 4096


# create socket that will use TCP and IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# setup connection with server
try:
    s.connect((HOST,PORT))
except:
    print("Something went wrong! Make sure that you are running server.py and that you are using the right port.");

print("Connection established on port", PORT,".")
print("You can now start sending messages here. Currently, the server should just echo the message back.")

while 1:
    # Receive data from server
    data = s.recv(SIZE)
    print ("RCVD: " + data.decode('utf-8'))

    # get input and send it to server send
    nb = str(input())
    print("Sending: " + nb)
    s.send(nb.encode('utf-8'));

# end connection. Although this should never happen because if infinite loop above
s.close()



# prints in red red
def red(name):
    print ("\033[91m {}\033[00m" .format(name))
red("hi")
