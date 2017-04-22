from socket import *

sequence = 0
done = "0"
playerNum = 0
connectMsg = "connect"
serverName = 'LukasBook.local'
serverPort = 12000

opp = "192.168.0.101"
oppPort = 0

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(connectMsg.encode(), (serverName, serverPort))
msg = clientSocket.recv(1024)
print(msg)
while done == "0":
    confirmP = clientSocket.recv(1024)
    print(confirmP)
    opp = clientSocket.recv(1024)
    print(opp)
    oppPort = int(clientSocket.recv(1024))
    print(oppPort)

    done = "1"

clientSocket.close()
