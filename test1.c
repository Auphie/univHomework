#include <stdio.h>

int main(){
    int i, j, start, end;
    int isPrime, sum=0;
    printf("Enter lower limit: ");
    scanf("%d", &start);
    printf("Enter upper limit: ");
    scanf("%d", &end);

    while(i<=end){
        i=start;
        isPrime = 1;
        for(j=2; j<=i/2 ;j++){
            if(i%j==0){
                isPrime = 0;
                break;
            }
        }
        if(isPrime==1){
            sum += i;
        }
    i=i+1;
    }
    printf("Sum of all prime numbers between %d to %d = %d", start, end, sum);

    return 0;
}
