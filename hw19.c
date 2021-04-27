#include<stdio.h>
#include<string.h>
#define SIZE 20

int dice(int face, int op){
	if (face==1 && op==1)
		return 3;
	else if (face==1 && op==2)
		return 4;
	else if (face==1 && op==3)
		return 5;
	else if (face==1 && op==4)
		return 2;
	else if (face==2 && op==1)
		return 3;
	else if (face==2 && op==2)
		return 4;
	else if (face==2 && op==3)
		return 1;
	else if (face==2 && op==4)
		return 6;
	else if (face==3 && op==1)
		return 6;
	else if (face==3 && op==2)
		return 1;
	else if (face==3 && op==3)
		return 5;
	else if (face==3 && op==4)
		return 2;
	else if (face==4 && op==1)
		return 1;
	else if (face==4 && op==2)
		return 6;
	else if (face==4 && op==3)
		return 5;
	else if (face==4 && op==4)
		return 2;
	else if (face==5 && op==1)
		return 3;
	else if (face==5 && op==2)
		return 4;
	else if (face==5 && op==3)
		return 6;
	else if (face==5 && op==4)
		return 1;
	else return 0;
}

void counts(int f1, int f2,int f3,int f4){
	int i, j, pair=0, result=0, numCount[7];
	for (i=1; i<7; i++)
		numCount[i]=0;
	numCount[f1]+=1;
	numCount[f2]+=1;
	numCount[f3]+=1;
	numCount[f4]+=1;
	for (i=1; i<=6; i++){
		printf("%d", numCount[i]);
		if (numCount[i]==4)
			pair += 4;
		else if (numCount[i]==2)
			pair += 1;
		else pair += 0;
	}
	if (pair==4)
		result=18;
	else if (pair==0)
		result =0;	
	else{
		for (i=6;i>=1;i--){
			if (numCount[i]==2){
				result=i*2;
				break;
			}
		}
	}
	printf("\n%d", result);
}

int main(void){
    int i,op1,op2,op3,op4, f1=1, f2=1, f3=1, f4=1, times, result=0;
    scanf("%d", &times);
	for (i=0;i<times; i++){
		scanf("%d %d %d %d",&op1,&op2,&op3,&op4);
		f1=dice(f1, op1);
		f2=dice(f2, op2);
		f3=dice(f3, op3);
		f4=dice(f4, op4);
	}
//	printf("%d,%d,%d,%d\n",f1,f2,f3,f4);
	counts(f1,f2,f3,f4);
	return 0;
}