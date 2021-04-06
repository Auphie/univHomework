#include <stdio.h>
#include <string.h>
#define SIZE 40

int main(void){
    int i, j, m;
    char input[SIZE];
    scanf("%s",input);
    scanf("%d",&m);
    char arr[m];
    size_t len = strlen(input);

    for (i=0; i<len-2; i++){
        for (j=i; j<i+3; j++){
            arr[j] = input[j];
        }
    printf("\n");
    }
}