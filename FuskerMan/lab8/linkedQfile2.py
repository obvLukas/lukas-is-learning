class Node():
    #en nod med attribut data och en pekare 
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedQ():
    #skapa privat attribut första nod och sista
    def __init__(self):
        self.__first = None
        self.__last = None

    #lägger till en nod i lista
    def enqueue(self, x):
        ny = Node(x) #objekt nod som heter ny
        if self.__first == None: #om det inte finns en nod, skapa ny som första och sista
            self.__first = ny
            self.__last = self.__first
        else: #annars sett senaste nods nextpekare till nya noden och sett sista till nya noden
            self.__last.next = ny
            self.__last = ny

    #tar bort objekt längst fram i kön
    def dequeue(self):
        if self.__first == None: #om första inte finns returnera inget
            return None
        else: #annars sätt variabeln data till första nodens data och next till första nodens nextpekare
            data = self.__first.data
            next = self.__first.next
            if next == None: #om next like med none sätt första och sista till None som i init
                self.__first = None
                self.__last = None
            else: #annars sätt första noden till det vi tidigare satte som next
                self.__first = next
            return data

    #kollar om attributen first och last är tomma
    def isEmpty(self):
        if self.__first == None and self.__last == None:
            return True
        else:
            return False
