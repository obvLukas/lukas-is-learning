# -*- coding: utf-8 -*-
# Lukas Hennicks 9509099033
# Simon Tönnes 9310261558


# Definierar testvektorer
testvec_1 = ['1','5','q','%','O','O','r','O','O','O','O','O','X']
testvec_2 = ['1','2','O','1']
testvec_3 = ['O','p','1','A','O','O','O','O','u','d']
testvec_4 = ['O','O','x','4','1','O','O','O','x','O','O','O','O']

# Hämtar funktionen som testar om en lista innehåller fem 'O' i rad.

from lab1_func import vec_search

# Använder funktionen på testvektorerna.

Vec_1_bool = vec_search(testvec_1, 'O', 5)
Vec_2_bool = vec_search(testvec_2, 'O', 5)
Vec_3_bool = vec_search(testvec_3, 'O', 5)
Vec_4_bool = vec_search(testvec_4, 'O', 5)

#Testar 5 'X' i rad i vektorn ['1', '3', 'X', 'X', 'X', 'X', 'X', 'W']

print "Vektor 1:  \nFörväntat utfall: True \nUtfall:", Vec_1_bool
print "Vektor 2:  \nFörväntat utfall: False \nUtfall:", Vec_2_bool
print "Vektor 3:  \nFörväntat utfall: False \nUtfall:", Vec_3_bool
print "Vektor 4:  \nFörväntat utfall: False \nUtfall:", Vec_4_bool
