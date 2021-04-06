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
}            //-'0' to become num rev=[3,2,1,0,0,0]

void Print(char n[]){
	int i;					// [3,2,1,0,0,0]
	for (i=LEN-1; i>0; i--) // from right to left
		if(n[i]!=0) break;	// when 0 then skip
	for (; i>=0; i--)		// till the first num		
		printf("%d", n[i]);
	printf("\n");
}

void Add(char a[], char b[], char ans[]){
    int i, carry;
    for(carry=i=0; i<LEN; i++){
        ans[i] = a[i] + b[i] + carry;
        carry = ans[i] / 10;
        ans[i]%=10;
    }
}

char check_negative(char a[], char b[]){
    int i, borrow, sign;
    for(borrow=i=0; i<LEN; i++) {
        sign = a[i]-b[i]-borrow;
        if (sign<0)   	borrow=1;
        else  			borrow=0;
	}
	return sign<0?'-':'+';
}

void Minus(char a[], char b[], char ans[]){
    int i, borrow;
    for(borrow=i=0; i<LEN; i++) {
		ans[i] = a[i]-b[i]-borrow;
        if(ans[i]<0) {
            borrow=1, ans[i]+=10; // -3 -> +7
        } else {
            borrow=0;
        }
	}
}

void Multiply(char a[], char b[], char ans[]){
	int i, j;
	for(i=0; i<LEN*2; i++)
		ans[i]=0;
	for(i=0; i<LEN; i++) {
		for(j=0; j<LEN; j++) {
			ans[i+j]+=a[j]*b[i];
			if(ans[i+j]>=10) {
				ans[i+j+1]+=ans[i+j]/10;
				ans[i+j]=ans[i+j]%10;
			}
		}
	}
}

int main(void){
	char a[LEN], b[LEN], ans[LEN*2], op, sign;
	scanf("%d",&op);
	Input(a);
	Input(b);
	sign=check_negative(a,b);
	switch(op) {
		case 1: Add(a, b, ans);break;
		case 2: if (sign=='-'){
					printf("-");
					Minus(b, a, ans);
					break;
				}
				else {
					Minus(a, b, ans);
					break;
				}
		case 3: Multiply(a, b, ans);break;
	}
	Print(ans);
}