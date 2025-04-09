import socket
import pickle
from Constants import *
class Network:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
        self.id = int(self.connect())
        
    def connect(self):
        self.socket.connect((Constants.SERVER_IP,Constants.PORT))
        return self.socket.recv(2048).decode('utf-8')
    
    def send(self,package):
        self.socket.send(pickle.dumps(package))
        return pickle.loads(self.socket.recv(2048))
        
    def rcv(self):
        return pickle.loads(self.socket.recv(2048))
    