#include <stdio.h>
#include <string.h>
#define LEN 9

void  Input(char reverse[LEN]){
	int i, len;
	char input[LEN];
	scanf("%s", input);
	len = strlen(input);
	for (i=0; i<LEN; i++)
		reverse[i]=0;
		printf("init reverse=%s", reverse);
	for (i=0; i<len; i++){
		reverse[i]=input[len-i-1]-'0';
		printf("input[%d]=%d ", i, input[len-i-1]-'0');
		printf("\nreverse[%d]=%d", i, reverse[i]);
	}
	printf("\nreverse=%s",reverse);
}

void decimalToBit(int n){
	int digit=8, k;
	for (int i=digit-1; i>=0; i--){
		k=n>>i;
		if (k&1==1)
			printf("1");
		else
			printf("0");
	}
}

int main(void){
	char a[LEN];
	Input(a);
	printf("a=%s\n", a);
	return 0; 
}