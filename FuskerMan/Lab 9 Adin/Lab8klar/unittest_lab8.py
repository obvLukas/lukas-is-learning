from lab_8v2 import *
import unittest #Unittest library importeras
class SyntaxTest(unittest.TestCase):

    def testmolekyl(self): #Testar molekyl
        mening ="Ag5" #Stringen som ska testas
        self.assertEqual(kolla_syntaxatom(mening), "Följer syntaxen") #Om kolla_syntaxatom skickar ut "Följer Syntaxen" är det OK

    def test_readLetter(self):
        Letter = skapaq("G")
        self.assertNotEqual(readLetter(Letter), "Ej stor bokstav.")

    def test_readletter(self):
        letter = skapaq("b")
        self.assertNotEqual(readletter(letter), "Ej liten bokstav eller så är 3e tecknet inte en siffra.")

    def test_readNummer(self):
        nummer = skapaq("5")
        self.assertNotEqual(readNummer(nummer), "Talet lästes in som inkorrekt.")
    
        
        



        
if __name__ == '__main__':
    unittest.main()
