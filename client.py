"""
BashChat Client Script
Author(s): Micah Hauge, ...(feel free to add your name here if you contributed)
Last Updated: 6/22/2016 by Micah Hauge

*****USAGE*****
Run client without specifying port (defaults to 9001):
    python3 client.py

Run server on a specific port:
    python3 client.py 1234

****NOTES BEFORE HACKING AWAY*****
1) If the port is already in use, you will get the following error or somthing similar:
       OSError: [Errno 98] Address already in use

   Simply try using a different port. Anything above 5000 should be safe.

2) The server must be run first and the server and client must be run on the same port (duh..)
   if you don't run them on the same port, you will get the following error (or something similar):
       OSError: [Errno 107] Transport endpoint is not connected

3) All messages exchanged between server and client must be a 'bytes-like' object.
   You can convert a string to a bytes object with: string.encode('encodingType')
   I have chosen to use utf-8 encoding because it appears to be the current standard.
   So, this is how to encode a strings before it is sent:
       myString.encode('utf-8')

   Also note that the receiving end can convert it back to can string with the following:
       myBytesObject.decode('utf-8')

GLFH!
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
