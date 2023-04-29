import socket
import json
ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 9680
print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)
while True:
    Input = input('Hey there: ')
    if(Input == "Authenticate"):
        print("ciao")
        ClientMultiSocket.send(str.encode(Input))
        data_Total = json.dumps({"a": "trevor", "b": "password"})
        ClientMultiSocket.send(data_Total.encode())
    elif Input == "Register":
        print("ciao")
        ClientMultiSocket.send(str.encode(Input))
        data_Total = json.dumps({"a": "aryan", "b": "sood"})
        ClientMultiSocket.send(data_Total.encode())
    else:
        ClientMultiSocket.send(str.encode(Input))
        res = ClientMultiSocket.recv(8192)
        print(res.decode('utf-8'))
        ClientMultiSocket.send(str.encode("156"))
ClientMultiSocket.close()