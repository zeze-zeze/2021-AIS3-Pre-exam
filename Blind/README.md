# MISC - Blind
## 題目原始碼
```
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/syscall.h>

int syscall_black_list[] = {};

void make_a_syscall()
{
    unsigned long long rax, rdi, rsi, rdx;
    scanf("%llu %llu %llu %llu", &rax, &rdi, &rsi, &rdx);
    syscall(rax, rdi, rsi, rdx);
}

int main()
{
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    puts("You can call a system call, then I will open the flag for you.");
    puts("Input: [rax] [rdi] [rsi] [rdx]");
    close(1);

    make_a_syscall();
    int fd = open("flag", O_RDONLY);
    char flag[0x100];
    size_t flag_len = read(fd, flag, 0xff);
    write(1, flag, flag_len);
    return 0;
}
```

## 解法
很明顯，有個 close(1) 把 stdout 關掉了，所以後面的 flag 印不出來。

但是 make_a_syscall 可以讓我們任意呼叫一個 syscall，所以可以用 sys_dup2 把現在被關掉的 stdout(1) 取代掉。

因此把 stderr 取代現有的 stdout，sys_dup2(33, 2, 1, 0) 就是答案
