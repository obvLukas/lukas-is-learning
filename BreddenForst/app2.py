# -*- coding: utf-8 -*-
from bintreeFile import Bintree
from linkedQFile import LinkedQ


def makechildren(startord, q):
    alfabet = list('abcdefghijklmnopqrstuvxyzåäö')
    letterNo = 0
    word = startord


    if word != slutord:
        while letterNo != 3:
            for letter in alfabet:
                word = list(word)
                word[letterNo] = letter
                s = ""
                word = s.join(word)
                if word in svenska and word not in gamla:
                    gamla.put(word)
                    q.enqueue(word)
                    #print(word)
            word = startord
            letterNo += 1
        return False

    else:
        print("Det finns en väg till", slutord)
        return True




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
    q.enqueue(startord)
    global gamla
    gamla = Bintree()
    gamla.put(startord)
#    makechildren(startord, q)

    foundWord = False

    while q.isEmpty() != True:
        nod = q.dequeue()
        #print(nod)
        if makechildren(nod, q):
            foundWord = True
            break
    if not foundWord:
        print("Det finns INTE en väg till", slutord)













if __name__ == '__main__':
    main()
