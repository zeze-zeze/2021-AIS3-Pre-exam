import pickletools

f = open('flag_checker.pkl', 'rb').read()
print(pickletools.dis(pickletools.optimize(f)))

'AIS3{dAmwjzphIj}'

'''
0: flag
1: __builtin__ getattr
2: [__builtin__ exit, __builtin__ str]
3: flag[9]
4: flag[1]

flag[5] = 'd'
flag[6] = 'A'
flag[7] = 'm'
flag[8] = 'w'
flag[9] = 'j'
flag[10] = 'z'
flag[11] = 'p'
flag[12] = 'h'
flag[13] = 'I' (flag[1])
flag[14] = 'j'
'''
