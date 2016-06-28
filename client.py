"""
BashChat Client Script
Author(s): Micah Hauge, Adam Mischke, ...(feel free to add your name here if you contributed)
Last Updated: 6/22/2016 by Micah Hauge
"""

import socket
import sys
from random import randint

# prints in red, gray, green, white, pink, and blue ANSI Escape sequences
def color(name):
    return ('\033[9' + str(randint(0,5)) + 'm' + '{}\033[00m' .format(name))


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

ID = color(str(input('Login: ')))  # login and get a color

print("Connection established on port", PORT,".")
print("You can now start sending messages here. Currently, the server should just echo the message back.")

while 1:
                   
    # Receive data from server
    data = s.recv(SIZE)
    print (ID + ':' , data.decode('utf-8'))

    # get input and send it to server send
    nb = str(input())
    
    # exit NEED SUGGESTIONS
    if (nb == ':q'):
        break                           # breaks the loop

    try:                                # try to send
        s.send(nb.encode('utf-8'));     
    except:                             # except and try again
        print("Couldn't send, try again")

# end connection. Although this should never happen because if infinite loop above
s.close()




