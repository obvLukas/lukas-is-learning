class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return self.val

class Bintree():
    def __init__(self):
        self.root = None

    def put(self, newvalue):
        if(self.root == None):
            self.root = Node(newvalue)
        else:
            self.putta(self.root, newvalue)

    def __contains__(self, value):
        if self.root != None:
            return self.finns(self.root, value)
        else:
            return False

    def write(self):
        if(self.root == None):
            print('There are no nodes...')
        else:
            if self.root != None:
                self.skriv(self.root)
        print("\n")

#    def isRight(self, str1, str2):
        #IMPORTERA LISTA MED ALFABET

    def putta(self, root, newvalue):
        if(newvalue < root.val):
            if(root.left != None):
                self.putta(root.left, newvalue)
            else:
                root.left = Node(newvalue)
        elif(newvalue > root.val):
            if(root.right != None):
                self.putta(root.right, newvalue)
            else:
                root.right = Node(newvalue)
        else:
            root = Node(newvalue)

    def finns(self, nod, val):
        if(val == nod.val):
            return True
        elif(val < nod.val and nod.left != None):
            return self.finns(nod.left, val)
        elif(val > nod.val and nod.right != None):
            return self.finns(nod.right, val)



    def skriv(self, nod):
        if(nod != None):
            self.skriv(nod.left)
            print(nod.val)
            self.skriv(nod.right)





svenska = Bintree()
#svenska.put("gurka")
#svenska.put("kebab")
#svenska.put("alv")
#svenska.put("slavsquat")
#svenska.put("mekatronik")
#svenska.write()

#       G
#   A       K
#                S
#             M


if 'mekatronik' in svenska:
    print('mekatronik finns i svenska')

#if 'jambalaya' in svenska:
#    print('Jambalaya finns i svenska')
