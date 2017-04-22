# Kod av Lukas Hennicks
# -*- coding: utf-8 -*-

class Pokedex():

    pokelist = []
    HPlist = []
    ATKlist = []
    DEFlist = []
    TYPElist = []


    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.TYPElist.append(self.type)

    def __str__(self):
        return '%s is a %s pokemon with %s HP, %s atk and %s def.' % (self.name, self.type, self.HP, self.ATK, self.DEF)

    def addNametoList(self):
        self.pokelist.append(self.name)

    def addHP(self, HP):
        self.HP = HP
        self.HPlist.append(self.HP)

    def addATK(self, ATK):
        self.ATK = ATK
        self.ATKlist.append(self.ATK)

    def addDEF(self, DEF):
        self.DEF = DEF
        self.DEFlist.append(self.DEF)




# Test Pokemon
#one = Pokedex('TestPoke', 'notype')
#one.addHP(100)
#one.addATK(35)
#one.addDEF(85)


#print(one)
#print("%s has: \n %s HP.") % (two.name, two.HP)


def read_file(filename):
    f=open(filename,"r")
    #print(f.read())
    f.readline()
    vec=[]
    for line in f:
        if line[0] != '#':
            vec.append(line.split(';'))
    f.close()
    return vec

pkvec = read_file('pkdx.csv')


#ADD ATTRIBUTES TO CLASS
for pokeId in range(0, len(pkvec)):
    tempName = pkvec[:][pokeId][2]
    tempHP = pkvec[:][pokeId][3]
    tempATK = pkvec[:][pokeId][4]
    tempDEF = pkvec[:][pokeId][5]
    tempTYPE = pkvec[:][pokeId][10]

    tempName = Pokedex(tempName,tempTYPE)
    tempName.addNametoList()
    tempName.addHP(tempHP)
    tempName.addATK(tempATK)
    tempName.addDEF(tempDEF)


def searchPoke(search):
    counter = 0
    for x in range(0, len(Pokedex.pokelist)):
        if Pokedex.pokelist[x].upper() == search.upper():
            return counter
            break
        else:
            counter += 1



print('-' * 50)
searchWord = raw_input('What pokemon do you want to know more about?\n')
print('-' * 50)

searchId = searchPoke(searchWord)

if searchId == None:
    print('%s is not a Pokemon.') % (searchWord)
else:
    print('%s is a %s pokemon with %s HP, %s atk and %s def.') % (Pokedex.pokelist[searchId], Pokedex.TYPElist[searchId], Pokedex.HPlist[searchId], Pokedex.ATKlist[searchId], Pokedex.DEFlist[searchId])
