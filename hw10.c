#include <stdio.h>
#include <math.h>

void GrayCode(int n, int k){
    if (n==1)
        printf("%d\n",k);
    else if (k < pow(2,(n-1))){
        printf("%d",0);
        return GrayCode(n-1, k);
    }
    else {
        printf("%d",1);
        return GrayCode(n-1, pow(2,n)-1-k);
    }
}

int main(void){
    int n, k, next=0;
    while (next != -1) {
        scanf("%d %d", &n, &k);
        GrayCode(n, k);
        scanf("%d", &next);
    }
}