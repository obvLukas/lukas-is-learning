from socket import *
import threading

class roomThread(threading.Thread):
    def __init__(self, name, client1IP, client1P, client2IP, client2P, port):
        threading.Thread.__init__(self)
        self.name = name
        self.client1 = (client1IP, client1P)
        self.client2 = (client2IP, client2P)
        self.port = port
        self.done = 0


def run(self):
    connectMsg = str(self.port)
    playerNum = 1
    sequence = 0
    roomSocket = socket(AF_INET, SOCK_DGRAM)
    roomSocket.bind(("192.168.0.101",self.port))

    roomSocket.sendto(connectMsg, self.client1)
    roomSocket.sendto(connectMsg, self.client2)

    roomSocket.sendto(self.client2[0], self.client1)
    roomSocket.sendto(str(self.client2[1]), self.client1)

    roomSocket.sendto(self.client1[0], self.client2)
    roomSocket.sendto(str(self.client1[1]), self.client2)
    print("Done..")


    #//GLOBALS
userID = 1
userList = ()
userPort = ()
roomID = 1
count = 0
client1 = ()
client2 = ()
done = 0
portNum = 12000
port = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("192.168.0.101", portNum))


while True:
    connectReq, userAddr = serverSocket.recvfrom(1024)
    userList += userAddr
    serverSocket.sendto(str(userID).encode(), userAddr)
    if userID%2 == 0 and .5*userID == roomID:
        pList = list(userList)
        port += 1
        room = roomThread(roomID, pList[count], pList[count + 1], pList[count + 2], pList[count + 3], port)
        room.start()
        count += 4
        roomID += 1
        print("Room created..")
    userID += 1
