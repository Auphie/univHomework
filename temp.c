#include <stdio.h>
#include <stdlib.h>


int eval(int n){
if (n==1) return 1;
else if (n==0) return 0;
else {
    n=n-2;
    eval(n)
}

int main(void){
    int n=3;
    printf("%d", eval(n))       
    return 0;
} 