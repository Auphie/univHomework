#include <stdio.h>
#include <string.h>
#define LEN 40

void Input(char reverse[]){
	char input[LEN];
	int i, size;
	for(i=0; i<LEN; i++)
		reverse[i]=0;       // create rev=[0,0,0,0,0,0]
	scanf("%s", input);     // scan s = '123'
	size=strlen(input);     // sizeof(s) = 3, i<size
	for(i=0; i<size; i++)   // rev[i] = s[size-i-1]  
		reverse[i] = input[size-i-1]-'0'; 
}                           // rev=[3,2,1,0,0,0]

void Print(char n[]){
	int i;
	for(i=LEN-1; i>0; i--)
		if(n[i]!=0) break;
	    else        printf("%d", n[i]);
	printf("\n");
}

void Add(char a[], char b[], char c[]){
	int i;
	for(i=0; i<LEN; i++)
		c[i]=a[i]+b[i];
	for(i=0; i<LEN-1; i++) {
		if(c[i]>=10) {
			c[i+1]+=c[i]/10;
			c[i]=c[i]%10;
		}
	}
}

int main(void){
	char a[LEN], b[LEN], c[LEN];
	Input(a);
	Input(b);
	Add(a, b, c);
	Print(c);
	return 1;
}