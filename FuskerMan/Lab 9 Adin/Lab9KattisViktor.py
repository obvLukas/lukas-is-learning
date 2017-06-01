import sys
atomer='H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','R','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Fl','Lv'


class Node:
    def __init__(self, ord = None):

        self.ord = ord
        self.parent = None

class LinkedQ:
    def __init__(self):    # Definierar privata attributer
       self.__first = None
       self.__last = None

    def enqueue(self,ord):
        """Stoppar in x sist i kön """
        self.new = Node(ord)
        if self.__first == None:  # Om tom blir både först och sist samma kort.
            self.__first=self.new
            self.__last=self.new

        else:
            self.__last.parent = self.new         # sista kortet får en next till nya kortet
            self.__last = self.new              # som sedan sätts till det sista

    def dequeue(self):
        """Plockar ut och returnerar det som står först i kön """
        if self.__first == None:  # Om kön är tom
            print('Kön är tom')
        else:
            z = self.__first.ord              # Första kortets värde sparas
            self.__first = self.__first.parent    # Första kortets "next-kort" sätts till nya första kort
            return z                            # Skriver ut det sparade värdet från tidigare

    def isEmpty(self):
        """Returnerar True om kön är tom, False annars """
        if self.__first == None:  # Om kön är tom är isEmpty True
             return True
        else:                     # Annars False
             return False
    def peek(self):
        if not self.isEmpty():
            return self.__first.ord
        else:
            return None

class Syntaxfel(Exception):
    pass

def storemol(molekyl):
    q=LinkedQ()
    for x in molekyl:
        q.enqueue(x)
    return q

def readformel(molekyl):
    q = storemol(molekyl)
    try:
        readmol(q)
        if q.peek() is not None:
            raise Syntaxfel('Felaktig gruppstart')
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as fel:
        return str(fel) + " vid radslutet " + str(printq(q))

def readmol(q):
    if q.peek() == None or q.peek() == ')':
        return
    readgroup(q)
    readmol(q)

def readgroup(q):
    if q.peek() == '(':
        q.dequeue()#(
        readmol(q)
        if q.peek() != ')':
            raise Syntaxfel('Saknad högerparentes')
        q.dequeue()#)
        if q.peek() != None and q.peek().isnumeric():
            readnum(q)
        else:
            raise Syntaxfel('Saknad siffra')
        return
    readatom(q)
    readnum(q)#kanske lägga till att det kan va None

def readatom(q):
    if q.peek().islower():
        raise Syntaxfel('Saknad stor bokstav')
    if q.peek().isnumeric():
        raise Syntaxfel('Felaktig gruppstart')
    A=q.dequeue()
    a=''
    if q.peek() != None and q.peek().islower():
        a=q.dequeue()
    if A+a in atomer:
        return
    else:
        raise Syntaxfel('Okänd atom')

def readnum(q):
    if q.peek() == None or not q.peek().isnumeric():
        return
    if q.peek() == '0':
        q.dequeue()
        raise Syntaxfel('För litet tal')
    tal='0'
    while q.peek() != None and q.peek().isnumeric():
        tal=tal + q.dequeue()
    if int(tal)<2:
        raise Syntaxfel('För litet tal')

def printq(q):
    a=''
    while q.peek() != None:
        a=a+q.dequeue()
    return a

def main():
    with open("test2.txt", "r", encoding = "utf-8") as textfile:
        for i in textfile:
            i2=i.strip()
            if i2 !='#':
                resultat = readformel(i2)
                print(resultat)
main()







