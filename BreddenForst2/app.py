# -*- coding: utf-8 -*-
from bintreeFile import Bintree
from linkedQFile import LinkedQ

class SolutionFound(Exception):
    pass

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def __str__(self):
        #return "Word: %s, Parent: %s \n" % (self.word, self.parent)
        return self.word

    def writechain(self, child):
        if child.parent != None:
            self.writechain(child.parent)
            print(child)
        else:
            print(child.word)


def makechildren(Nod, q):
    alfabet = list('abcdefghijklmnopqrstuvxyzåäö')
    letterNo = 0
    word = Nod.word

    if word != slutord:
        while letterNo != 3:
            for letter in alfabet:
                word = list(word)
                word[letterNo] = letter
                s = ""
                word = s.join(word)
                if word in svenska and word not in gamla:
                    gamla.put(word)
                    nyNod = ParentNode(word, Nod)
                    q.enqueue(nyNod)
                    #print(word)
            word = Nod.word
            letterNo += 1
    else:
        raise SolutionFound


def readfile(filename):

    f = open('word3.txt', "r",encoding = "utf-8")

    svenska = Bintree()
    for line in f:
        word = line.strip()
        if word not in svenska:
            svenska.put(word)
    f.close()
    return svenska


def main():
    global svenska
    svenska = readfile('word3.txt')
    startord = input("Ange Startord: \n")
    global slutord
    slutord = input("Ange Slutord: \n")
    print("\n")

    q = LinkedQ()
    global gamla
    gamla = Bintree()
    gamla.put(startord)

    startNod = ParentNode(startord)
    q.enqueue(startNod)

    foundWord = False

    while q.isEmpty() != True:
        Nod = q.dequeue()
        #print(Nod)
        try:
            makechildren(Nod, q)
        except SolutionFound:
            print("Det finns en väg till", slutord,": ")
            Nod.writechain(Nod)
            break
    print("Det finns INTE en väg till", slutord)



if __name__ == '__main__':
    main()
