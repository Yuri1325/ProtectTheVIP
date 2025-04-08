class Package:
    def __init__(self,client_id,player):
        self.client_id = client_id
        self.player = player
        self.client_id = client_id
        self.childPackages = []
    def getPlayer(self):
        return self.player
    def setPlayer(self,player):
        self.player = player
    def getClient_Id(self):
        return self.client_id
    def getChildrenList(self):
        return self.childPackages
