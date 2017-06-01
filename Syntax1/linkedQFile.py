class Node():

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

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
        temp = self.first
        self.first = self.first.next
        self.size = self.size - 1
        return temp

    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.first.val


    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
