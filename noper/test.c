#include <stdio.h>
int main(){
    for(int i=0; i<9; i++){
        printf("%d\n", rand() & 0x3f);
    }
}
