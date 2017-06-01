# -*- coding: utf-8 -*-
from syntax import *
import unittest
from linkedQFile import LinkedQ

class SyntaxTest(unittest.TestCase):

    def testMolekyl(self):
        self.assertEqual(trySyntax("Ha12"), "Korrekt Syntax!")

    def testFelMolekyl(self):
        self.assertEqual(trySyntax("ha12"), "Felaktig Syntax!")

if __name__ == '__main__':
    unittest.main()
