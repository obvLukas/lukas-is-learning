from lab_9 import *

from atom_info import atom_dict







#i = "Si(C3(COOH)2)4(H2O)7/n"
i= "QxSi(C3(COOH)2)4(H2O)7Ag5"
print("Molekyl: ", i)


def readmole(i):
    q=skapaq(i)
    mol = readformel(q)
    return mol
    
    
    
    

mol = readmole(i)
mg=Molgrafik()
mg.show(mol)

atom_dict = atom_dict()
print(atom_dict['Si'])
print(atom_dict['C'])
print(atom_dict['O'])
print(atom_dict['H'])

def weight(mol):
    vikt = 0
    if mol.down != None:
        vikt = vikt + weight(mol.down)*mol.num
    if mol.next != None:
        vikt = vikt + weight(mol.next)


    vikt = vikt + float(atom_dict[mol.atom])*mol.num
    
    return vikt


print("Vikten av molekylen:", str(weight(mol)) + "g/mol")







  
           


    
    
        

                
    
