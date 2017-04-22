# -*- coding: utf-8 -*-
# Lukas Hennicks 9509099033
# Simon Tönnes 9310261558


def read_file(filename):
    f=open(filename,"r")
    #print(f.read())
    f.readline()
    vec=[]
    for line in f:
        if line[0] != '#':
#            print line
            vec.append(line.strip().split(' '))

    f.close()
#    print vec
    return vec

def main():

    mat = read_file('text.txt')
    from row_func import row_search
    from col_func import col_search
    from diag_func_down_new import diag_search_down
    #from diag_func_up import diag_search_up

    row_bool = row_search(mat, 'X', 5)
    col_bool = col_search(mat, 'X', 5)
    diag_bool_down = diag_search_down(mat, 'X', 5)
    diag_bool_up = diag_search_up(mat, 'X', 5)
#    print row_bool
#    print col_bool
#    print diag_bool_down
#    print diag_bool_up


    if row_bool or col_bool or diag_bool_down or diag_bool_up == True:
        print 'Fem i rad!'
    else:
        print 'Det saknas 5 i rad'






if __name__ == '__main__':
     main()
