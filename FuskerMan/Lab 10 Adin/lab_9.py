from linkedQFile import LinkedQ
import string
from molgrafik import *



    
def RepresentsInt(s): #Stackoverflow kollar om stringen s är int, hjälpfunktion
    try: 
        int(s)
        return True
    except ValueError:
        return False




class Syntaxfel(Exception): #Egendefinierad exception
    pass

def gora_atomlista(filename):
        with open(filename, "r", encoding = "utf-8") as textfile:
            lista=textfile.read().splitlines()

        lista2=""
                
        for i in range(0,5):
            lista2= lista2 +" "+ lista[i]
            
            
            

        return lista2


def readformel(q):
    

    return readmol(q)

def readmol(q):
##    if q.peek() ==")":
##        return
    rutan = readgroup(q)
    if q.isEmpty() == False and q.peek() != "\n":
        #if q.peek() == "(" or q.peek().isupper() == True: #Denna ska hantera H20)Fe\n
        rutan.next = readmol(q)
    return rutan

def readmol2(q):
    rutan = readgroup(q)

    if q.isEmpty() == False and q.peek() ==")":
        
        return rutan
    
    
    if q.isEmpty() == False and q.peek() != "(" and q.peek().isupper()==False:
        raise Syntaxfel("Saknad stor bokstav vid radslutet"+q.make_string())
    
        
     
    if q.isEmpty() == False and q.peek() != "\n" and q.peek()!=")":
        #if q.peek() == "(" or q.peek().isupper() == True: #Denna ska hantera H20)Fe\n
        rutan.next = readmol2(q)
    return rutan
    

def readgroup(q):

    rutan = Ruta()
      
        
    if q.isEmpty() == False and q.peek() =="(": #Denna ska hantera okej slutparenteser
        #print("1 iteration i startparentes (  ")
        b=q.dequeue()
        rutan.down =readmol2(q)
        if q.isEmpty() == True or q.peek() !=")":
            raise Syntaxfel("Saknad högerparentes vid radslutet")
            
        else:
        
            b= q.dequeue()      
            rutan.num = readNummer(q)
            return rutan
    #print(q.peek(), "atomen som skickas in till readAtom")

    rutan.atom =readAtom(q)
    if q.isEmpty() == False and RepresentsInt(q.peek()) == True:
        
        rutan.num = readNummer(q)

    

    return rutan
    

        
            


        

def readAtom(q): #Läser atomsyntax
    atomlista=gora_atomlista("Lista_atomer.txt")
    
    L =readLetter(q)
    
    l=" "
    
    if q.isEmpty() == False and q.peek().islower():

        l = readletter(q)
        if (L +l) not in atomlista:
            raise Syntaxfel("Okänd atom vid radslutet" +q.make_string())
        return L+l
    
    if (L +l) not in atomlista:
        raise Syntaxfel("Okänd atom vid radslutet" +q.make_string())
    return L
            
        

def readLetter(q):  #Läser stor bokstav
    if q.isEmpty() == True:
        raise Syntaxfel("Felaktig gruppstart vid radslutet")
        
    g=q.peek()
    #print(g, "readLetter")
    
    
    
    if g.isupper(): #Kollar om det är storbokstav
        Letter = q.dequeue() 
        return Letter
    if g.islower():
        raise Syntaxfel("Saknad stor bokstav vid radslutet" +q.make_string())
    raise Syntaxfel("Felaktig gruppstart vid radslutet" +q.make_string())

def readletter(q): #Läser små bokstäver
    g=q.peek()
    #print(g, "readletter")
    letter = q.dequeue()
    
    if letter.islower(): #Kollar om liten bokstav, och om nästa efter det är ett tal
        return letter
      
    raise Syntaxfel("Ej liten bokstav eller så är 3e tecknet inte en siffra.")



def readNummer(q): #Funktionen som läser nummer
    d=q.peek()
    #print(d, "Readnummer")
    summa_str = ""
    
    if q.isEmpty() == False and RepresentsInt(q.peek()) == False:
        
        
        raise Syntaxfel("Saknad siffra vid radslutet" + q.make_string())

    else:
        summa_str=q.dequeue()
        if q.isEmpty() == False and int(summa_str)==0:
            raise Syntaxfel("För litet tal vid radslutet" + q.make_string())
            
            
        
        if q.isEmpty() == False and RepresentsInt(q.peek()) == False and int(summa_str)<2:
            
            raise Syntaxfel("För litet tal vid radslutet" + q.make_string())

        while q.isEmpty() == False and RepresentsInt(q.peek()) == True: #Krav: Nummer och >1
            b=q.dequeue()
            summa_str= summa_str + b
        
    


    
    
    return int(summa_str)


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

      
        q.enqueue(c)

    return q




def main ():


##    molekylens_namn = input("Vänligen skriv molekylens namn: ")
##    resultat = kolla_syntaxatom(molekylens_namn)
##    print(resultat)

    return
main()
