"""
BashChat Server Script
Author(s): Micah Hauge, ...(feel free to add your name here if you contributed)
Last Updated: 6/22/2016 by Micah Hauge

*****USAGE*****
Run server without specifying port (defaults to 9001):
    python3 server.py

Run server on a specific port:
    python3 server.py 1234

****NOTES BEFORE HACKING AWAY*****
1) If the port is already in use, you will get the following error or somthing similar:
       OSError: [Errno 98] Address already in use

   Simply try using a different port. Anything above 5000 should be safe.

2) All messages exchanged between server and client must be a 'bytes-like' object.
   You can convert a string to a bytes object with: string.encode('encodingType')
   I have chosen to use utf-8 encodeing because it appears to be the current standard.
   So, this is how to encode all strings before they are sent:
       myString.encode('utf-8')

   Also note that the receiving end can convert it back to can string with the following:
       myBytesObject.decode('urf-8')

3) Notice that a new thread is created for each incoming connection.
   This is to allow multiple clients to be served at a time.

GLFH!

"""

import socket
import select
import logging
import sys
from _thread import *

# set HOST to '' so the bind() method will fill in the address of the local machiene
HOST = ''
PORT = None

# use specified port if it was given by user, else use port 8000
if sys.argv[1:]:
    PORT = int(sys.argv[1])
else:
    PORT = 9001

# max number of connetions to be queued at a time
BACKLOG = 10

# number of bites to receive at a time. Should be plenty for a simple chatroom
SIZE = 4096

# create socket that will use TCP and IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the current host, and the port specified above
# this will fail if a process is already using that port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print(msg)
    sys.exit()

print("Socked bind complete.")

# listen for connections
s.listen(BACKLOG)
print("SERVER: Listening on PORT", PORT)


# function to handle connections (in a seperate threads)
def client_thread(conn):
    # Notice the string is converted to a bytes object by calling .encode
    conn.send('THIS IS INITIAL PING FROM THE SERVER'.encode('utf-8'))

    # Receive initial message (this is for debuging purposes and can be removed later)
    # data = conn.recv(SIZE)
    # print("SERVER: rcvd '" + data.decode('utf-8') + "' from client.")

    while True:
        # Receive data from client
        data = conn.recv(SIZE)
        print("SERVER: rcvd '" + data.decode('utf-8') + "' from client.")

        if not data:
            break

        # send reply to client
        reply = 'ECHO FROM SERVER: ' + data.decode('utf-8')
        conn.sendall(reply.encode('utf-8'))

        print("SERVER: sending '" + data.decode('utf-8') + "' back to client.")
    # close connection.
    conn.close()

# infinite loop to serve clients. Opens new threads so that multiple clients can be served
while True:
    # accept connection
    client, address = s.accept();
    print("SERVER: conencted with " + address[0] + ":" + str(address[1]))

    # starts serving client in a seperate thread
    start_new_thread(client_thread, (client,))

# stop server
s.close()

print("EXIT");
