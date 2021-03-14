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
            m=(m+1)/2;
        }
    }
    return counts;
}

int bitToDecimal(char n[]){
    int decimal;
    for (int i=0; i<8;i++)
        decimal=(decimal<<1)+n[i]-'0';
    return decimal;
}

void decimalToBin(int n){
    int k;
    for (int i = 3; i >= 0; i--)  {
        k = n >> i;
        if (k & 1)
        printf("1");
        else
        printf("0");
    }
    printf("\n");
}

int main(void){
    int decimal, counts, Sum=0;
    decimal = 125;
    for (int i=decimal; i>=0; i--){
        counts = simuCounts(i);
        Sum+=counts;
        printf("i=%d, c=%d\n", i, counts);
    }
printf("sum=%d",Sum);
return 0;
}