# -*- coding: utf-8 -*-

from linkedQFile import LinkedQ

class SyntaxError(Exception):
    pass

def isInteger(num):
    try:
        int(num)
        return True
    except:
        return False

def isLetter(char):
    alphabet = 'abcdefghijklmnopqrstuvxyz'

    for letter in alphabet:
        if char.upper() == letter.upper():
            return True
    return False


def readBigLetter(q):
    Node = q.dequeue()
    bigLetter = Node.val

    if bigLetter.isupper():
        return
    else:
        raise SyntaxError("The letter has to be upper-case.")

def readSmallLetter(q):
    Node = q.dequeue()
    smallLetter = Node.val

    if smallLetter.islower():
        return
    else:
        raise SyntaxError("The letter has to be lower-case.")

def readNumber(q):
    num = q.dequeue()
    integer = num.val

    if isInteger(integer):
        integer = int(integer)
        if integer < 1:
            raise SyntaxError("The number has to be > 1.")
        elif integer == 1:
            if isInteger(q.peek()):
                return
            else:
                raise SyntaxError("The number cannot be 1.")
        else:
            return

    else:
        raise SyntaxError("The character has to be a number.")

def readAtom(q):
    readBigLetter(q)
    if isLetter(q.peek()):
        readSmallLetter(q)
        return
    elif isInteger:
        return
    else:
        raise SyntaxError("The second character has to be a letter")

def readMolecule(q):
    readAtom(q)
    if isInteger(q.peek()):
        readNumber(q)
    else:
        raise SyntaxError("The molecule syntax requires a number.")


def trySyntax(testsubj):
    q = LinkedQ()

    for char in testsubj:
        q.enqueue(char)

    try:
        readMolecule(q)
        return "Korrekt Syntax!"
    except SyntaxError:
        return "Felaktig Syntax!"



def main():

    return

main()
