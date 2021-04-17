#include <stdio.h>
#include <string.h>
#define SIZE 40

int check_repetition(char arr[], int m, int start){
    int i, j;
    for (i=start; i<start+m-1; i++){
        for (j=i+1; j<start+m; j++) {
            if (arr[i]==arr[j]){
                return 0;
            }
        }
    }
    return 1;
}

int main(void){
    int i, j, k, m, result=0;
    char input[SIZE];
    scanf("%s",input);
    scanf("%d",&m);
    size_t len = strlen(input);
    for (i=0; i<len-m+1; i++){
        result += check_repetition(input, m, i);
    }
    printf("%d", result);
}