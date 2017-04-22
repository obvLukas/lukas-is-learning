# -*- coding: utf-8 -*-
# Lukas Hennicks 9509099033
# Simon Tönnes 9310261558

# MODIFIERAD


def diag_search_down(mat, var_search, vecsize):

    from lab1_func import vec_search

    width, height = len(mat[0]), len(mat)
    def diag(sx, sy):
        for x, y in zip(range(sx, height), range(sy, width)):
            yield mat[x][y]
    for sx in range(height):
        yield list(diag(sx, 0))
    for sy in range(1, width):
        yield list(diag(0, sy))


    for n in range(len(width)):
        temp_diag.append(diag)
        print temp_diag
