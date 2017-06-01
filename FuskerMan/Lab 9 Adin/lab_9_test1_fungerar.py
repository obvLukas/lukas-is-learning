from linkedQFile import LinkedQ
import string

    
def RepresentsInt(s): #Stackoverflow kollar om stringen s är int, hjälpfunktion
    try: 
        int(s)
        return True
    except ValueError:
        return False




class Syntaxfel(Exception): #Egendefinierad exception
    pass


def readformel(q):

    readmol(q)

def readmol(q):
    
    readgroup(q)
    if q.isEmpty() == False and q.peek() != "\n":
        if q.peek() != ")":
            readmol(q)

def readgroup(q):    
        
    if q.peek() =="(":
        #print("1 iteration i startparentes (  ")
        b=q.dequeue()
        readmol(q)
        if q.peek() !=")":
            raise Syntaxfel("Saknad högerparentes vid radslutet")
            
        else:
        
            b= q.dequeue()      
            readNummer(q)
            return        

    readAtom(q)
    if q.isEmpty() == False and RepresentsInt(q.peek()) == True:
        
        readNummer(q)
        
            

def readMolekyl(q): #Läser Molekylsyntax
    readAtom(q)
    while q.isEmpty() == False and RepresentsInt(q.peek()) == True : #Så länge det finns något i kön och nästavärde verkar vara nummer, readnummer
            
            readNummer(q)
            
            
            
    if q.isEmpty() == False: #Om kön inte är tom så kollar vi om nästa är en bokstav eller siffra
        readNummer(q)
        

def readAtom(q): #Läser atomsyntax
    
    readLetter(q)
    
    if q.isEmpty() == False and q.peek().islower():

        readletter(q)
            
        

def readLetter(q):  #Läser stor bokstav
    g=q.peek()
    #print(g, "readLetter")
    Letter = q.dequeue() 
    
    
    if Letter.isupper(): #Kollar om det är storbokstav
        return
    raise Syntaxfel("Ej stor bokstav.")

def readletter(q): #Läser små bokstäver
    letter = q.dequeue()
    if letter.islower(): #Kollar om liten bokstav, och om nästa efter det är ett tal
        return
      
    raise Syntaxfel("Ej liten bokstav eller så är 3e tecknet inte en siffra.")



def readNummer(q): #Funktionen som läser nummer
    d=q.peek()
    #print(d, "Readnummer")
    
    if q.isEmpty() == False and RepresentsInt(q.peek()) == False:
        
        raise Syntaxfel("Saknad siffra vid radslutet")
    
    while q.isEmpty() == False and RepresentsInt(q.peek()) == True and int(q.peek())>1: #Krav: Nummer och >1
        b = q.dequeue()

    if q.isEmpty() == False and RepresentsInt(q.peek()) == True and int(q.peek())<1:
        raise Syntaxfel("För litet tal vid radslutet")

    
    
    return


def kolla_syntaxatom(molekylens_namn): #Tar in en string som argument för att kolla om det följer syntax

    
    q= LinkedQ() #Skapar länkad kö
    
    for c in molekylens_namn: #For loop över string, tar ut enskilda bokstäver
      
        q.enqueue(c)        

    try:
        readMolekyl(q) #Testar syntax för molekyl
        return "Följer syntaxen" #Felmeddelande
    except Syntaxfel as a:
        return a

def skapaq(string):
    q = LinkedQ()
    for c in string: #For loop över string, tar ut enskilda bokstäver

        if c != "\n":
      
            q.enqueue(c)

    return q




def main ():


##    molekylens_namn = input("Vänligen skriv molekylens namn: ")
##    resultat = kolla_syntaxatom(molekylens_namn)
##    print(resultat)

    return
main()
