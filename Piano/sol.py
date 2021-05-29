from z3 import *

index = [
'C',
'D',
'E',
'F',
'G',
'A',
'B',
'CSharp',
'DSharp',
'FSharp',
'GSharp',
'ASharp'
]

l1 = [14,17,20,21,22,21,19,18,12,6,11,16,15,14]
l2 = [0,-3,0,-1,0,1,1,0,6,0,-5,0,1,0]

push = [BitVec('p{}'.format(i), 8) for i in range(14)]

s = Solver()
for i in range(14):
    s.add(push[i] + push[(i+1) % 14] == l1[i])
    s.add(push[i] - push[(i+1) % 14] == l2[i])

print(s.check())
m = s.model()
for i in range(14):
    print(index[int(str(m[push[i]]))])
