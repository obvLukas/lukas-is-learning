# -*- coding: utf-8 -*-

class Hashtabell():

    def __init__(self, size):
        self.size = size
        self.NodeList = [None] * self.size
        self.krockCount = 0

    def makeHash(self, word):
        hash = 5381

        for i in range(0, len(word)):
           hash = ((hash << 5) + hash) + ord(word[i])
    #    print(int(hash))
        return hash%self.size

    def put(self, data, newNode):
        hashval = self.makeHash(data)

        if self.NodeList[hashval] == None:
            self.NodeList[hashval] = newNode
        elif self.NodeList[hashval] == data:
            self.NodeList[hashval].data = newNode.data
        else:
            self.krockCount += 1
            for i in range(0,len(self.NodeList)):
                hashval = (hashval + i)%self.size
                if self.NodeList[hashval] == None:
                    self.NodeList[hashval] = newNode
                    break
                elif self.NodeList[hashval] == data:
                    self.NodeList[hashval].data = newNode.data
                    break


    def get(self, data):
        hashval = self.makeHash(data)

        for i in range(0, len(self.NodeList)):

            if self.NodeList[hashval].namn == data:
                return self.NodeList[hashval]

            else:
                hashval = (hashval + 1)%self.size
        raise KeyError
