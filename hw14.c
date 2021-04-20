#include <stdio.h>
#define SIZE 5

int noDuplicate(int data[]){
    int result = 1;
    for (int i=0; i<3; i++){
        for (int j=i+1; j<4; j++){
            if (data[i]==data[j])
                return 0;
        }
    }
    return 1;
}

void checkAB(char ans[], char guess[], int *a, int *b){
    int i, j;
    *a=0; *b=0;
    for (i=0; i<4; i++){
        if (guess[i]==ans[i])
            (*a)++;
        for (j=0; j<4; j++){
            if (i!=j && guess[j]==ans[i]){
                (*b)++;}
        }
    }
}

int main(void){
    int a=0, b=0, guessTimes=6;
    char ans[SIZE], guess[SIZE];
    fflush(stdin);
    scanf("%s", ans);
    for (int i=0; i<guessTimes; i++){
        scanf("%s", guess);
        checkAB(ans, guess, &a, &b);
        if (a==4){
            printf("win\n");
            break;
        }
        else
            printf("%dA%dB\n", a, b);
    }
    return 1;
}