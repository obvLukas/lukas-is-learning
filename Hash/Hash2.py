# -*- coding: utf-8 -*-
import timeit

class HashNode():
    def __init__(self, hashval, data):
        self.hashval = hashval
        self.data = data

    def __str__(self):
        return "Artist name: %s. Hashvalue:  %s." % (self.data, str(self.hashval))


class Hashtabell():

    def __init__(self):
        self.size = 2000003
        self.NodeList = [None] * self.size
        self.krockCount = 0

#    def makeHash(self, word):
#        self.word = word
#        array = list(self.word)
#        hashkey = ""
#        for letter in array:
#            hashkey += str(ord(letter))
#        return int(hashkey)%self.size

#    //Better Hash

    def makeHash(self, word):
        hash = 5381

        for i in range(0, len(word)):
           hash = ((hash << 5) + hash) + ord(word[i])
    #    print(int(hash))
        return hash%self.size

    def store(self, data):
        hashval = self.makeHash(data)
        newNode = HashNode(hashval,data)
        #print(self.hashval)
        #print(newNode)
        #self.linprobe(HashPos, newNode)

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



    def quadratic(self, i):
        return (i**2)%self.size


    def search(self, data):
        hashval = self.makeHash(data)

        for i in range(0, len(self.NodeList)):

            if self.NodeList[hashval].data == data:
                return self.NodeList[hashval]

            else:
                hashval = (hashval + 1)%self.size


    def __str__(self):
        return str(self.NodeList)


def readfile(filename):

    print('Läser in fil...')
    artistTable = Hashtabell()
    f = open(filename, "r", encoding = "utf-8")
    for line in f:
        data = line.strip().split('<SEP>')
        artistTable.store(data[2])
    f.close()
    print('Fil inläst...')
    return artistTable




def main():

    art_obj = readfile('unique_tracks.txt')


    print("-" * 50)
    print("Gör linjärsökning...")
    tid = timeit.timeit(stmt = lambda: art_obj.search('Shakira'), number = 10000)
    print("Hashade sökningen tog", round(tid, 4) , "sekunder")













if __name__ == '__main__':
    main()
