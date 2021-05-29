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
