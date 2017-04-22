# -*- coding: utf-8 -*-
# Lukas Hennicks 9509099033
# Simon Tönnes 9310261558

def row_search(mat, var_search, vecsize):

    from lab1_func import vec_search
    #    print vec

    for row in mat:
#        print row
        rows_bool = vec_search(row, 'X', 5)
#        print rows_bool
        if rows_bool == True:
            return rows_bool

    return rows_bool
