import string

out = open('output.txt', 'rb').read().strip().split(b': ')[1]
print(out.hex())
keys = [0 for i in range(4)]
keys[0] = (out[0] - ord('3')) % 96
keys[1] = (out[1] - ord('S')) % 96
keys[2] = (out[2] - ord('I')) % 96
keys[3] = (out[3] - ord('A')) % 96
print(keys)
flag = ''
for i in range(len(out)):
    c = (out[i] - keys[i % 4]) % 96
    while chr(c) not in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~':
        c += 96
    flag += chr(c)

assert len(flag) == len(out)
print(flag.encode().hex())

flag = ''.join([flag[i:i+4][::-1] for i in range(0, len(flag), 4)])
print(flag)
