# -*- coding: utf-8 -*-
from linkedQfile2 import LinkedQ
import string


def RepresentsInt(s): #Stackoverflow
    try:
        int(s)
        return True
    except ValueError:
        return False


molekylens_namn = input("V�nligen skriv molekylens namn: ")
q= LinkedQ()
temp_num = 0
for c in molekylens_namn:

##    if RepresentsInt(c) == True
##        temp_num = int(c) + temp_num
##
    q.enqueue(c)



class Syntaxfel(Exception):
    pass

def readMolekyl(q):
    readAtom(q)
    if q.peek() > 1:
        readNummer(q)


def readAtom(q):
    readLetter(q)
    if q.peek().islower():
        readletter(q)


def readLetter(q):
    Letter = q.dequeue
    if Letter.isupper():
        return
    raise Syntaxfel("Ej stor bokstav.")

def readletter(q):
    letter = q.dequeue
    if letter.islower():
        return
    raise Syntaxfel("Ej liten bokstav.")



def readNummer(q):

    nummer = q.dequeue
    if q.peek() > 1 and q.peek() < 10:

        return
    raise Syntaxfel("Talet l�stes in som inkorrekt.")
