# -*- coding: utf-8 -*-
# Lukas Hennicks 9509099033
# Simon Tönnes 9310261558

def col_search(mat, var_search, vecsize):

    from lab1_func import vec_search
    col_bool = False
    n = 0
    col_num = 0
    col_vec = range(len(mat))

    while n < len(mat):
        for col in mat[col_num][n]:
            if col_num < len(mat):
                col_vec[col_num] = col
                col_num += 1
            else:
                print col_vec
                col_bool = vec_search(col_vec, var_search, vecsize)
                if col_bool == True:
                    return col_bool
                    col_num = 0

    print col_vec
    n += 1
    print n

    return col_bool
