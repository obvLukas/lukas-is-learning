from linkedQFile import LinkedQ
import string


def RepresentsInt(s): #Stackoverflow
    try: 
        int(s)
        return True
    except ValueError:
        return False




class Syntaxfel(Exception):
    pass

def readMolekyl(q):
    readAtom(q)
    while RepresentsInt(q.peek()) == True:
        if int(q.peek()) > 1:
            readNummer(q)
            
            v =q.dequeue()
            
    readNummer(q)
        

def readAtom(q):
    readLetter(q)
    if q.peek().islower():
        readletter(q)
    

def readLetter(q):    
    Letter = q.dequeue()
    
    
    if Letter.isupper():
        return
    raise Syntaxfel("Ej stor bokstav.")

def readletter(q):
    letter = q.dequeue()
    if letter.islower() and RepresentsInt(q.peek()) == True:
        return
    raise Syntaxfel("Ej liten bokstav.")



def readNummer(q):
    
    nummer = q.dequeue
    if RepresentsInt(q.peek()) == True and int(q.peek()) > 1 and int(q.peek()) < 10:
        return
    raise Syntaxfel("Talet lästes in som inkorrekt.")


def main ():
    molekylens_namn = input("Vänligen skriv molekylens namn: ")
    
    q= LinkedQ()
    temp_num = 0
    for c in molekylens_namn:
        #print(c)
##    if RepresentsInt(c) == True
##        temp_num = int(c) + temp_num
##        
        q.enqueue(c)
        

    try:
        readMolekyl(q)
        print("Följer syntaxen")
    except Syntaxfel as a:
        print(a)

    return
main()
