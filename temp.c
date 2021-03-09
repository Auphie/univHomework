#include <stdio.h>

int f(int n){
    if (n==1)
        return 1;
    else if (n%2==0){
        n = n-1;
        return n+f(n-2);
    }
    else
        return n+f(n-2);
}

int main(){
    printf("%d",f(8));
    return 0;
}