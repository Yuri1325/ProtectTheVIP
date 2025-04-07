import socket
from _thread import *
import pickle
from Constants import *
from Package import * 
import Player
class Server:
    def __init__(self,ip):
        socket = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
        try:
            socket.bind((ip,Constants.PORT))
        except Exception as e:
            print(f"[CONNECTION FAILED] {e}")
        socket.listen(4)
        print("[SERVER STARTED] Waiting for Connections....")

        clientCounter = 0
        packageList = [Package(0,Player()),Package(1,Player()),Package(2,Player()),Package(3,Player())]

        def runClient(conn,client_id):
            global packageList,clientCounter
            conn.send(pickle.dumps(packageList[client_id]))
            sendingMessage = None
            while True:
                try:
                    receivedMessage = pickle.loads(conn.recv(2048))
                    packageList[client_id] = receivedMessage
                    if not receivedMessage:
                        break 
                    else:
                        sendingMessage = pickle.loads(start_new_thread(getOtherPackages,(client_id)))
                
                except Exception as e:
                    print(f"[CLIENT ERROR] {e}")
                conn.sendall(sendingMessage)
            print(f"[CLIENT DISCONECTED] @ {conn}")
            clientCounter -=1

        def getOtherPackages(client_id):
            global packageList
            newList = []
            for x in packageList:
                if x.client_id != client_id:
                    newList.append(x)
            return newList

        while True:
            conn,addr = socket.accept()
            start_new_thread(runClient,(conn,clientCounter))
            clientCounter+=1
            print(f"[NEW CONNECTION] @ {conn}")
