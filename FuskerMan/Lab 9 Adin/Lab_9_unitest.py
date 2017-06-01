from lab_9 import *
import unittest #Unittest library importeras
class SyntaxTest(unittest.TestCase):


    
    with open("test2.txt", "r", encoding = "utf-8") as textfile: #Öppnar filen
        lista =[]
        
       
        for i in textfile:
            if i != "#":
                q = skapaq(i)

        
                try:
                      
                    readformel(q)
                    print("Formeln är syntaktiskt korrekt")
                except Syntaxfel as a:
                    print(a)

    
    
    
    
    
    def gora_atomlista(filename):
        with open(filename, "r", encoding = "utf-8") as textfile:
            lista=textfile.read().splitlines()

        lista2=""
                
        for i in range(0,5):
            lista2= lista2 +" "+ lista[i]
            
            
            

        return lista2
            
    lista2=gora_atomlista("Lista_atomer.txt")
    #print(lista2)
##    if "h" in lista2:
##        print("ja")
##    else:
##        print("Nej")
##    
    
           
           


    
    
        

                
    
