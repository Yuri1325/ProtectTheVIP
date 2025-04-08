import socket
from _thread import *
import pickle
from Constants import *
from Package import * 
from Player import *

socket = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
try:
    socket.bind((Constants.SERVER_IP,Constants.PORT))
except Exception as e:
    print(f"[CONNECTION FAILED] {e}")
socket.listen(4)
print("[SERVER STARTED] Waiting for Connections....")

clientCounter = 0
packageList = [Package(0,Player(0,True)),Package(1,Player(1,True)),Package(2,Player(2,True)),Package(3,Player(3,True))]

def runClient(conn,client_id):
    global packageList,clientCounter
    conn.send(str(client_id).encode())
    sendingMessage = None
    while True:
        
        try:
            receivedMessage = pickle.loads(conn.recv(2048))
            packageList[client_id] = receivedMessage
            sendingMessage =getOtherPackages(client_id)
            conn.sendall(pickle.dumps(sendingMessage))
        except Exception as e:
            print(f"[CLIENT ERROR] {e}")
        
    print(f"[CLIENT DISCONECTED] @ {conn}")
    clientCounter -=1

def getOtherPackages(client_id):
    global packageList
    p = Package(client_id,None)
    for x in packageList:
        if x.client_id != client_id:
            p.childPackages.append(x)
    return p

while True:
    conn,addr = socket.accept()
    start_new_thread(runClient,(conn,clientCounter))
    clientCounter+=1
    print(f"[NEW CONNECTION] @ {conn}")
