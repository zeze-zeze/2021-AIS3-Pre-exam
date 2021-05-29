# CRYPTO - Microchip
## 程式原始碼
其中引入的 python.h 就只是讓這個 .c 檔案可以寫得像是 python 而已

```
#include "python.h"


def track(name, id) -> str ꞉                                                    {

    if len(name) % 4 == 0 ꞉                                                     ){
        padded = name + "4444"                                                  ;}
    elif len(name) % 4 == 1 ꞉                                                   ){
        padded = name + "333"                                                   ;}
    elif len(name) % 4 == 2 ꞉                                                   ){
        padded = name + "22"                                                    ;}
    elif len(name) % 4 == 3 ꞉                                                   ){
        padded = name + "1"                                                     ;}

    keys = list()                                                               ;
    temp = id                                                                   ;
    for i in range(4) ꞉                                                         ){
        keys.append(temp % 96)                                                  ;
        temp = int(temp / 96)                                                   ;}

    result = ""                                                                 ;
    for i in range(0, len(padded), 4) ꞉                                         ){

        nums = list()                                                           ;
        for j in range(4) ꞉                                                     ){
            num = ord(padded[i + j]) - 32                                       ;
            num = (num + keys[j]) % 96                                          ;
            nums.append(num + 32)                                               ;}

        result += chr(nums[3])                                                  ;
        result += chr(nums[2])                                                  ;
        result += chr(nums[1])                                                  ;
        result += chr(nums[0])                                                  ;}

    return result                                                               ;}


def main() -> int ꞉                                                             {

    name = open("flag.txt", "r").read().strip()                                 ;
    id = int(input("key = "))                                                   ;

    print("result is:", track(name, id))                                        ;
    return 0                                                                    ;}
```

## 解法
重點就是在 keys 是未知的，但是因為 flag 前面一定是 AIS3，所以可以跟 output.txt 的前 4 個 byte 逆回去，這樣就得到 key 了。

## exploit
```
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
```

* flag: `AIS3{w31c0me_t0_AIS3_cryptoO0O0o0Ooo0}`
