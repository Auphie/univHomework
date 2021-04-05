#include <stdio.h>
#include <string.h>
#define LEN 6

void Print(int n[]){
	int i;
	for(i=5; i>0; i--)
		if(n[i]!=0) break;
	for(; i>=0; i--)
		printf("%d", n[i]);
	printf("\n");
}

int main(void){
	int c[6]={3,2,1,0,0,0};
	Print(c);
	return 1;
}