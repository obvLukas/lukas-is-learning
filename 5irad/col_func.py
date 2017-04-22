# -*- coding: utf-8 -*-
# Lukas Hennicks 9509099033
# Simon Tönnes 9310261558

def col_search(mat, var_search, vecsize):

    from lab1_func import vec_search

    col_bool = None
    col_vec = []

    for col in range(len(mat[0])):
        for row in range(len(mat)):
            col_vec.append(mat[row][col])
        #print(col_vec)
        col_bool = vec_search(col_vec, 'X', 5)
        if col_bool == True:
            return col_bool
        col_vec = []
    return col_bool
