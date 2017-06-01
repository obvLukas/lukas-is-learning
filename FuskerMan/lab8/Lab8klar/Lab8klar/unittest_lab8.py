from lab_8v2 import *
import unittest #Unittest library importeras
class SyntaxTest(unittest.TestCase):

    def testmolekyl(self): #Testar molekyl
        mening ="Mn4" #Stringen som ska testas
        self.assertEqual(kolla_syntaxatom(mening), "Följer syntaxen") #Om kolla_syntaxatom skickar ut "Följer Syntaxen" är det OK


if __name__ == '__main__':
    unittest.main()
