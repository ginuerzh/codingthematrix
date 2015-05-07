from vec import Vec
from triangular import *

# Exercise 2.11.4
D = {0, 1, 2}
rowlist = [Vec(D, {0:1, 1:3, 2:2}), Vec(D, {1:2, 2:4}), Vec(D, {2:-10})]
b = [7,4,12]
ans = triangular_solve_n(rowlist, b)
#print(ans)

# Section 2.11.5
label_list = ['a','b','c','d']
D = set(label_list)
rowlist=[Vec(D,{'a':4, 'b':-2,'c':0.5,'d':1}), Vec(D,{'b':2,'c':3,'d':3}),
    Vec(D,{'c':5, 'd':1}), Vec(D,{'d':2.})]
b = [6, -4, 3, -8]
ans = triangular_solve(rowlist, label_list, b)
#print(ans)

# Section 2.12 Lab: Comparing voting records using dot-product
# Task 2.12.1
def create_voting_dict(strlist):
    dct = dict()
    for ent in strlist:
        a = ent.split(' ')
        votes = list()
        for i in range(3, len(a)):
            votes.append(int(a[i]))
        dct[a[0]] = votes
    return dct

voting_dict = create_voting_dict(list(open('voting_record_dump109.txt')))
#print(len(voting_dict))
#print(voting_dict)

# Task 2.12.2
def policy_compare(sen_a, sen_b, voting_dict):
    return sum([a*b for (a,b) in zip(voting_dict[sen_a], voting_dict[sen_b])])

dot = policy_compare('Brownback', 'Murray', voting_dict)
print(dot)
dot = policy_compare('Roberts', 'Rockefeller', voting_dict)
print(dot)

# Task 2.12.3
def most_similar(sen, voting_dict):
    most = -100
    nm = ''
    for k in voting_dict.keys():
        dot = policy_compare(sen, k, voting_dict)
        if sen != k and dot > most:
            most = dot
            nm = k
    return nm

print(most_similar('Akaka', voting_dict))

# Task 2.12.4
def least_similar(sen, voting_dict):
    least = 100
    nm = ''
    for k in voting_dict.keys():
        dot = policy_compare(sen, k, voting_dict)
        if sen != k and dot < least:
            least = dot
            nm = k
    return nm

print(least_similar('Akaka', voting_dict))

