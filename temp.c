#include <stdio.h>
#include <stdlib.h>

int GCD(int up, int down){
	if (down!=0)
		return GCD(down, up%down);
	return up;
}

int LCM(int up, int down){
	int lcm, gcd;
	gcd = GCD(up, down);
	lcm = up*down/gcd;
	return lcm;
}

void Reduction(int up, int down){
	int gcd, quotient, remainder;
	float result;
	gcd = GCD(up, down);
	up/=gcd;
	down/=gcd;
	result = (double)up/down;
	quotient=up/down;
	if (result>0.0){
		if (quotient>0){
			remainder=up%down;
			printf("%d(%d/%d)\n", quotient, remainder, down);
		}
		else printf("%d/%d\n", up, down);
	}
	else if (result<0.0){
		if (abs(quotient)>0){
			remainder=up%down;
			printf("-%d(%d/%d)\n", abs(quotient), abs(remainder), abs(down));
		}
		else printf("-%d/%d\n", abs(up), abs(down));
	}
	else
		printf("0\n");
}

void Add(int up1, int down1, int up2, int down2){
	int up, down, lcm;
	printf("%d/%d + %d/%d is ", up1, down1, up2, down2);
	lcm = LCM(down1, down2);
	up = up1*down2+up2*down1;
	down = lcm;
	Reduction(up, down);
}

int main(){
    int up1, up2, down1, down2, gcd, lcm;
	up1=-23; up2=2;
	down1=4; down2=3;
	Add(up1, down1, up2, down2);
    return 0;
}