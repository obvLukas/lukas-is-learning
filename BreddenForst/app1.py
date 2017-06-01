# -*- coding: utf-8 -*-
from bintreeFile import Bintree


def makechildren(startord):
    alfabet = list('abcdefghijklmnopqrstuvxyzåäö')
    letterNo = 0
    word = startord
    gamla = Bintree()
    gamla.put(startord)

    if word != slutord:
        while letterNo != 3:
            for letter in alfabet:
                word = list(word)
                word[letterNo] = letter
                s = ""
                word = s.join(word)
                if word in svenska and word not in gamla:
                    gamla.put(word)
                    #print(word)
            word = startord
            letterNo += 1

    return gamla

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

    gamla = makechildren(startord)
    gamla.write()










if __name__ == '__main__':
    main()
