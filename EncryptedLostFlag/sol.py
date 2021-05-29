from pwn import *
import numpy as np
from sympy import Matrix

def calc_sub_1420(a1, a2):
    ret = [0 for i in range(36)]
    for v8 in range(6):
        for i in range(6):
            for j in range(6):
                ret[j + v8 * 6] = (ret[j + v8 * 6] + a2[j + i * 6] * a1[i + v8 * 6]) % 257
    return ret

def sub_1540(ipt, last4):
    Some1_v4 = [0 for i in range(36)]
    for i in range(6):
        Some1_v4[7 * i] = 1

    while last4:
        if last4 & 1:
            Some1_v4 = calc_sub_1420(Some1_v4, ipt)
        
        ipt = calc_sub_1420(ipt, ipt)
        
        last4 >>= 1
    return Some1_v4

def sub_1600(a1, a2):
    return calc_sub_1420(a1, sub_1540([ord(i) for i in a2], u32(a2[-4:])))

target = [ord(c) for c in 'How do you inverse faster pow calc!!']

unk_2058 = [i for i in open('chall', 'rb').read()[0x2058:0x2058 + 36]]
unk_2080 = [i for i in open('chall', 'rb').read()[0x2080:0x2080 + 36]]

def arr2np(arr):
    return np.array([arr[i:i+6] for i in range(0, len(arr), 6)])

matrix_2058 = arr2np(unk_2058)
inv_matrix_2058 = np.linalg.inv(matrix_2058)
mod_inv_matrix_2058 = np.array(Matrix(matrix_2058).inv_mod(257))
matrix_2080 = arr2np(unk_2080)
matrix_target = arr2np(target)

pow_ipt = mod_inv_matrix_2058.dot(matrix_target)
matrix_flag = matrix_2080.dot(pow_ipt) % 257

flag = ''
for i in range(6):
    for j in range(6):
        flag += chr(int(matrix_flag[i][j]))
print(flag)
