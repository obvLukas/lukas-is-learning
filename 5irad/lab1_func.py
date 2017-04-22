# -*- coding: utf-8 -*-
# Lukas Hennicks 9509099033
# Simon Tönnes 9310261558

def vec_search(testvec, var_search, NumInRow):
    count = 0
    O_exist = False
    for char in testvec:
        if char == var_search:
            count += 1
            if count == NumInRow:
                O_exist = True
        else:
            count = 0

    return O_exist
