class User():
    agelist = []
    a = None
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.agelist.append(age)

    def __contains__(self, age):
        print self.findAge(0,age)
        return self.findAge(0, age)

    def findAge(self, root, val):
        if self.agelist[root] == val:
            return True
        else:
            return self.findAge(root+1, val)


Lukas = User('lukas', '21')
Kent = User('Kentaboy', '18')
Smeb = User('smeb', '125')

print(Lukas.agelist)
print(Kent.agelist)
print(Smeb.agelist)

if '5' in Kent:
    print('YAAAAAAAAAAAAAAS')
