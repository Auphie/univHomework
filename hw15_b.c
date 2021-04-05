#include <stdio.h>
#include <string.h>
#define SIZE 20

void add(char a[], char b[], char ans[], int size){
    int i, carry=0;
    for (i=size-1; i>=0; i--){
        ans[i]=(a[i]+b[i]+carry-96)%10+'0';
        printf("ans[%d]=%c\n", i, ans[i]);
        carry =(a[i]+b[i]+carry-96)/10;
    }
    if (carry > 0)
        ans[i]='1';
}

void print(char ans[], int size){
    int i;
    for (i=size; i>=0; i--){
        printf("ans[%d]=%c",i , ans[i]);
    }
}

int main(void){
    int size;
    char a[SIZE], b[SIZE];
//    scanf("%d", operator_type);
    scanf("%s", a);
    scanf("%s", b);
    size = strlen(a)>strlen(b)?strlen(a):strlen(b);
    char ans[size*2];
    add(a, b, ans, size);
    print(ans, size);
    return 1;
}