# BashChat
BashChat is a simple but elegant chat room application that can be run within bash.

## Usage
run client and server without specifying port (defaults to 9001):
    python3 client.py
    python3 server.py

Run client and server on a specific port (must be the same.. duh):
    python3 client.py 1234
    python3 server.py 1234

## Before you start hacking
1) If the port is already in use, you will get the following error or something similar:
       OSError: [Errno 98] Address already in use

   Simply try using a different port. Anything above 5000 should be safe.


2) The server must be run first and the server and client must be run on the same port (duh..)
   if you don't run them on the same port, you will get the following error (or something similar):
       OSError: [Errno 107] Transport endpoint is not connected

3) All messages exchanged between server and client must be a 'bytes-like' object.
   You can convert a string to a bytes object with: string.encode('encodingType')
   I have chosen to use utf-8 encodeing because it appears to be the current standard.
   So, this is how to encode all strings before they are sent:
       myString.encode('utf-8')

   Also note that the receiving end can convert it back to can string with the following:
       myBytesObject.decode('urf-8')

4) Notice that a new thread is created for each incoming connection.
   This is to allow multiple clients to be served at a time.

GLFH!

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
## Credits
Author(s): Micah Hauge, (feel free to add your name here)
