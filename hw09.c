#include <stdio.h>
#include <math.h>

void grayCode(int n, int k){
    if (n==1)
        printf("%d\n",k);
    else if (k < pow(2,(n-1))){
        printf("%d",0);
        return grayCode(n-1, k);
    }
    else {
        printf("%d",1);
        return grayCode(n-1, pow(2,n)-1-k);
    }
}

int main(void){
    int n, k, next=0;
    while (next != -1) {
        scanf("%d %d", &n, &k);
        grayCode(n, k);
        scanf("%d", &next);
    }
}