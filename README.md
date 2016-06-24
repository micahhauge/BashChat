# BashChat
BashChat is a simple but elegant chat room application that can be run within bash.

## Usage
To run client and server without specifying port (defaults to 9001):
```
python3 client.py
python3 server.py
```
To run client and server on a specific port (must be the same.. duh):
```
python3 client.py 1234
python3 server.py 1234
```
Currently the server simply echos the messages sent to it by the client back to the client.

## A few things before you start hacking
If the ports you are trying to use are already in use, you will get the following error or something similar:
```
OSError: [Errno 98] Address already in use
```
Simply try using a different port. Anything above 5000 should be safe.


The server must be run first and the server and client must be run on the same port (duh). If you don't run them on the same port, you will get the following error (or something similar):
```
OSError: [Errno 107] Transport endpoint is not connected
```


All messages exchanged between server and client __must__ be a '_bytes-like_' object. You can convert a string to a bytes object with:
```python
string.encode('encodingType')
```
I have chosen to use utf-8 encoding because it appears to be the current standard. So, this is how you should encode all strings before they are sent:
```python
myString.encode('utf-8')
```
Also note that the receiving end can convert it back to can string with the following:
```python
myBytesObject.decode('urf-8')
```

Notice that a new thread is created for each incoming connection. This is to allow multiple clients to be served at a time.

__Be sure to write good comments and descriptive commit messages! GLFH and happy coding!__

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
## Credits
Author(s): Micah Hauge, (feel free to add your name here)
