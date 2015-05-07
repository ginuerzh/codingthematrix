from dictutil import *
'''
# task 0.5.30
L = dict2list({'a':'A', 'b':'B', 'c':'C'}, ['b','c','a'])
print(L)

#task 0.5.31
dct = list2dict(['A','B','C'], ['a','b','c'])
print(dct)

#task 0.5.32
def all_3_digit_numbers(base, digits):
    return {x*base**2+y*base+z for x in digits for y in digits for z in digits}
print(all_3_digit_numbers(2, {0,1}))
print(all_3_digit_numbers(3, {0,1,2}))
print(all_3_digit_numbers(10, {0,1,2,3,4,5,6,7,8,9}))

#task 0.6.4
print(listrange2dict(['A','B','C']))
'''

# task 0.6.6
def makeInverseIndex(strlist):
    dct = {}
    for (i,s) in enumerate(strlist):
        for w in s.split():
            if w in dct:
               dct[w].add(i)
            else:
                dct[w] = {i}
    return dct

dct = makeInverseIndex(list(open('stories_small.txt')))
#print(dct)

#task 0.6.7
def orSearch(inverseIndex, query):
    s = set()
    for w in query:
        if w in inverseIndex:
            s = s | inverseIndex[w]
    return s

#print(orSearch(dct, ['without', 'who']))

#task 0.6.8
def andSearch(inverseIndex, query):
    s = set()
    for w in query:
        if w in inverseIndex:
            if len(s) == 0:
                s = inverseIndex[w]
            else:
                s = s & inverseIndex[w]
    return s
print(andSearch(dct, ['medical']))