import string

table = 'AlS3{BasE64_i5+b0rNIng~\\Qwo/-xH8WzCj7vFD2eyVktqOL1GhKYufmZdJpX9}'
encoded = 'BgiJ6\\w1Aj\\1guikl7xiXKIhXKil6fo65Kn87B-8warzK==='
flag = '' # 5 * n + 1
index = []
for e in encoded:
    for i in range(len(table)):
        if e == table[i]:
            index.append(i)

print(index)

cs = [4, 2, 3, 5, 6, 0, 3, 4, 3, 4, 4, 4, 3, 7, 3, 1, 3, 4, 6, 5, 5, 1, 1, 4, 5, 0, 4, 5, 7, 7, 4, 1, 5, 7, 1, 5, 7, 4, 5, 1, 4, 3, 1, 4, 7, 3, 2, 1]

rs = [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]

assert len(cs) == len(encoded) and len(rs) == len(encoded)

bits = ''
for i in range(len(index)):
    b = index[i] + (cs[i] << 6) + (rs[i] << 9)
    bits += bin(b)[2:].rjust(10, '0')

flag = ''
for i in range(0, len(bits), 8):
    flag += chr(int(bits[i:i+8], 2))
print(flag)
