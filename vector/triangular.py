# Copyright 2013 Philip N. Klein
from vec import Vec
from vecutil import zero_vec

def triangular_solve_n(rowlist, b):
    '''
    Solves an upper-triangular linear system.
    rowlist is a nonempty list of Vecs.  Let n = len(rowlist).
    The domain D of all these Vecs is {0,1, ..., n-1}.
    b is an n-element list or a Vec whose domain is {0,1, ..., n-1}.
    The linear equations are:
       rowlist[0] * x = b[0]
                     ...
       rowlist[n-1] * x = b[n-1]
    The system is triangular.  That means rowlist[i][j] is zero
    for all i, j in {0,1, ..., n-1} such that i >j.

    This procedure assumes that rowlist[j][j] != 0 for j=0,1, ..., n-1.

    The procedure returns the Vec x that is the unique solution
    to the linear system.
    
    >>> D = {0, 1, 2}
    >>> rowlist = [Vec(D, {0:1, 1:3, 2:2}), Vec(D, {1:2, 2:4}), Vec(D, {2:-10})]
    >>> b = [7,4,12]
    >>> triangular_solve_n(rowlist, b)
    Vec({0, 1, 2},{0: -3.8000000000000007, 1: 4.4, 2: -1.2})
    '''
    D = rowlist[0].D
    n = len(D)
    assert D == set(range(n))
    x = zero_vec(D)
    for j in reversed(range(n)):
        x[j] = (b[j] - rowlist[j] * x)/rowlist[j][j]
    return x

def triangular_solve(rowlist, label_list, b):
    '''
    Solves an upper-triangular linear system.
    rowlist is a nonempty list of Vecs.  Let n = len(rowlist).
    b is an n-element list or a Vec over domain {0,1, ..., n-1}.
    The linear equations are:
       rowlist[0] * x = b[0]
                     ...
       rowlist[n-1] * x = b[n-1]
    label_list is a list consisting of all the elements of D,
    where D is the domain of each of the vectors in rowlist.
    The system is triangular with respect to the ordering given
    by label_list.  That means rowlist[n-1][d] is zero for
    every element d of D except for the last element of label_list,
    rowlist[n-2][d] is zero for every element d of D except for
    the last two elements of label_list, and so on.

    This procedure assumes that rowlist[j][label_list[j]] != 0
    for j = 0,1, ..., n-1.

    The procedure returns the Vec x that is the unique solution
    to the linear system.
    
    >>> label_list = ['a','b','c','d']
    >>> D = set(label_list)
    >>> rowlist=[Vec(D,{'a':4, 'b':-2,'c':0.5,'d':1}), Vec(D,{'b':2,'c':3,'d':3}), \
    Vec(D,{'c':5, 'd':1}), Vec(D,{'d':2.})]
    >>> b = [6, -4, 3, -8]
    >>> triangular_solve(rowlist, label_list, b)
    Vec({'d', 'b', 'c', 'a'},{'d': -4.0, 'b': 1.9, 'c': 1.4, 'a': 3.275})
    '''
    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(D))):
        c = label_list[j]
        row = rowlist[j]
        x[c] = (b[j] - x*row)/row[c]
    return x
