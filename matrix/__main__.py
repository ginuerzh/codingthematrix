from mat import Mat

M=Mat(({'a','b'}, {'@', '#', '?'}), {('a','@'):1, ('a','#'):2,
('a','?'):3, ('b','@'):10, ('b','#'):20, ('b','?'):30})

print(M)

M = Mat(({1,3,5}, {'a'}), {(1,'a'):4, (5,'a'): 2})

print(M)

print(M[1,'a'])
print(M[3,'a'])
