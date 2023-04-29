import socket
import os
from _thread import *
import psycopg2
import random
import json
server_socket = socket.socket()
host = '127.0.0.1'
port = 5680
try:
    conn = psycopg2.connect(database="postgres",
                        host="204.216.215.242",
                        user="app",
                        password="emptiness",
                        port="5432")
    print("Connection successful!")
except:
    print("Connection failed!")
cur = conn.cursor()
cur.execute("SELECT * FROM quiz")
rows_M = cur.fetchall()
cur.execute("SELECT * FROM quiz01")
rows_S = cur.fetchall()
try:
    server_socket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
server_socket.listen(socket.SOMAXCONN)

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    User = "Username"
    Password = "Password"
    while True:
        data = connection.recv(2048)
        if data.decode('utf-8') == "Start_Challenge":
            User_List_S = rows_S
            User_List_M = rows_M
            random.shuffle(User_List_S)
            random.shuffle(User_List_M)
            Multiple_Send = []
            Single_Send = []
            Multiple_Send.append(User_List_M[0])
            Multiple_Send.append(User_List_M[1])
            Multiple_Send.append(User_List_M[2])
            Multiple_Send.append(User_List_M[3])
            Multiple_Send.append(User_List_M[4])
            Single_Send.append(User_List_S[0])
            Single_Send.append(User_List_S[1])
            Single_Send.append(User_List_S[2])
            Single_Send.append(User_List_S[3])
            Single_Send.append(User_List_S[4])
            data_Total = json.dumps({"a": Single_Send, "b": Multiple_Send})
            print(data_Total)
            socket.send(data_Total.encode())
            point_return = connection.recv(2048)
            point = 1000
            
        if data == "LeaderBoard":
            Board_Sending = score_board.fetchall()
            data_Total = json.dumps({"a": Board_Sending})
            socket.send(data_Total.encode())
            print("SendLeaderboard")
        if data == "Authenticate":

            data = connection.recv(2048)
            print("authenticate")


        #connection.sendall(str.encode(response))
    connection.close()



while True:
    Client, address = server_socket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
ServerSideSocket.close()