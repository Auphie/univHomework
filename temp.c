#include <stdio.h>

int main() {
    char *p = "lose";
    char *str = "test";
    p = str; // "lose"字串遺失
//    (*str) = 'p'; //不可以指標解參考修改，
    for (int i=0; i<10; i++){
        printf("%c\n", *str);
        str++;
    }
    return 0;
}