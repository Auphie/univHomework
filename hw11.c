#include <stdio.h>

int simuCounts(int m){
    int counts=0;
    while (1){
        if (m==1 || m==0)
            break;
        else if (m%2==0){
            counts+=1;
            m=m/2;
        }
        else {
            counts+=1;
            m=(m+1)/2;;
        }
    }
    return counts;
}

int bitToDecimal(char *n){
    int decimal=0;
    int i;
    for (i=0; i<8;i++)
        decimal=(decimal<<1)+n[i]-'0';
    return decimal;
}

void decimalToBin(int n){
    int digit = 11, k;
    for (int i = digit-1; i >= 0; i--)  {
        k = n >> i;
        if (k&1 == 1)
            printf("1");
        else
            printf("0");
    }
    printf("\n");
}

int main(void){
    int i, next=0;
    while (next != -1) {
        int decimal=0, counts=0, total=0;
        char bitN[9];
//        fflush(stdin);
        scanf("%s", bitN);
        decimal = bitToDecimal(bitN);
        for (i=1; i<=decimal; i++){
            counts = simuCounts(i);
            total+=counts;
        }
        decimalToBin(total);
//        fflush(stdin);
        scanf("%d", &next);
    }
return 0;
}