class Node():

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


#TEST should give 5 & 21
#q = Node(5)
#q.setNext(21)
#print(q.getVal())
#print(q.getNext())

class LinkedQ():

    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None
        self.temp = None

    def getSize(self):
        return self.size

    def enqueue(self, val):
        newNode = Node(val)
        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode


        self.size += 1

    def dequeue(self):
        self.temp = self.first
        self.first = self.first.next
        return self.temp


    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

#TESTING LINKED LIST
#s = LinkedQ()
#s.enqueue(5)
#s.enqueue(3)
#s.enqueue(10)
#x = s.dequeue()
#y = s.dequeue()
#z = s.dequeue()
#print(x)
#print(y)
#print(z)
