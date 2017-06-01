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
    while q.isEmpty() == False and RepresentsInt(q.peek()) == True :
            
            readNummer(q)
            
            
            
    if q.isEmpty() == False:
        readNummer(q)
        

def readAtom(q):
    readLetter(q)
    if q.isEmpty() == False and q.peek().islower():
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
    raise Syntaxfel("Ej liten bokstav eller så är 3e tecknet inte en siffra.")



def readNummer(q):
    
    nummer = q.dequeue()
    if RepresentsInt(nummer) == True and int(nummer)>1:
        return
    raise Syntaxfel("Talet lästes in som inkorrekt.")

def kolla_syntaxatom(molekylens_namn):

    
    q= LinkedQ()
    
    for c in molekylens_namn:
      
        q.enqueue(c)        

    try:
        readMolekyl(q)
        return "Följer syntaxen"
    except Syntaxfel as a:
        return a



def main ():


##    molekylens_namn = input("Vänligen skriv molekylens namn: ")
##    resultat = kolla_syntaxatom(molekylens_namn)
##    print(resultat)

    return
main()
