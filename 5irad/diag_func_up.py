# -*- coding: utf-8 -*-
# Lukas Hennicks 9509099033
# Simon Tönnes 9310261558

# MODIFIERAD


def diag_search_up(mat, var_search, vecsize):

    from lab1_func import vec_search

    diag_bool = None
    updiag_bool = None
    lowdiag_bool = None
    lowdiag_vec = []
    updiag_vec = []
    lowtot_vec = []
    uptot_vec = []

    for updiagno in range(len(mat)):
        for n in range(len(mat[0])-updiagno):
            if 0 <= n+updiagno < len(mat[0]):
                updiag_vec.append(mat[len(mat)-n-1-updiagno][n])
        uptot_vec.append(updiag_vec)
        updiag_vec = []

    for lowdiagno in range(len(mat)):
        for n in range(len(mat[0])-lowdiagno):
            if 0 <= n+lowdiagno < len(mat[0]):
                lowdiag_vec.append(mat[len(mat)-n-1][n+lowdiagno])
        lowtot_vec.append(lowdiag_vec)
        lowdiag_vec = []

    #print lowtot_vec
    #print "--------------------------"
    #print uptot_vec

    for it_lowbool in range(0,len(lowtot_vec)):
        lowdiag_bool = vec_search(lowtot_vec[it_lowbool], 'X', 5)
        if lowdiag_bool == True:
            return lowdiag_bool
        else:
            for it_upbool in range(0, len(uptot_vec)):
                updiag_bool = vec_search(uptot_vec[it_upbool], 'X', 5)
                if updiag_bool == True:
                    return updiag_bool


    return diag_bool
