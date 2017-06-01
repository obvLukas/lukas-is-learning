import string
class Node:
    def __init__ (self, value, n=None):         #Skapar Node med vÃ¤rde och pointer
        self.value= value
        self.next= n
    def get_next(self):
        return self.next
    def get_value(self):
        return self.value
    def set_next(self, g=None):
        self.next=g
    def __str__(self):
        return value
class LinkedQ:
    def __init__(self):
        self.first= None                #Pekar pÃ¥ fÃ¶rsta elementet
        self.last= None                 #Pekar pÃ¥ sista elementet

    def enqueue(self, x):
        nynod=Node(x)
        nynod.set_next(None)
        if self.first == None:          #Om kÃ¶n Ã¤r tom frÃ¥n bÃ¶rjar pekar bÃ¥de first och last pÃ¥ samma element
            self.first = nynod
            self.last =nynod
        else:
            self.last.set_next(nynod)      #Om det redan finns nÃ¥got i kÃ¶n kÃ¶rs denna kod
            self.last = nynod

    def dequeue(self):
        if self.first == self.last:  #Kollar om det Ã¤r det sista elementet kvar, behÃ¶vs fÃ¶r isEmpty()
            item=self.first.get_value()
            self.last=None
            self.first=None
            return item
        else:
            item=self.first.get_value()
            nasta=  self.first.get_next()
            self.first= nasta
            return item

    def isEmpty(self):
        if (self.first==None) and (self.last==None): #Kollar om kÃ¶n Ã¤r tom
            return True
        else:
            return False

    def peek(self):
        return self.first.get_value()

