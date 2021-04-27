#include<stdio.h>
#include<string.h>
#define SIZE 20

void plot(int width, int step, int x_init, int y_init){
	int x, y;
	x=x_init+(step+1)/2;
	if (y%2==0)
        y=y_init+1;
    else
        y=y_init+0;
	printf("width=%d, x=%d, y=%d \n", width, x, y);
}

void plot2(int width, int x_init, int y_init){
	int i, j, x, y;
	for (i=0; i< width; i++){
		for (j=0; j< width; j++){
			y=y_init+i; x=x_init+j;
			printf("width=%d, init_x=%d, init_y=%d, x=%d, y=%d \n", width, x_init,y_init, y);
		}
	}
}

void square(char data[SIZE], int width, int* i, int* order){
    int step=0, len=strlen(data), x_init=0, y_init=0;
    while((*i)<len){
        step++;
        *order=step;
        if(data[*i]=='2'){
            (*i)++;
            square(data, width/2, i, order);
        }
        else if(data[*i]=='1'){
            x_init=((*order-1)/2);
			y_init=((*order-1)/2);
			printf("0_width=%d, order=%d, step=%d, x_init=%d, y_init=%d \n", width, *order, step, x_init, y_init);
            (*i)++;
			if (width == 1)
				plot(width, step, x_init, y_init);
			else
				plot2(width, y_init, x_init);
        }
        else if(data[*i]=='0'){
            (*i)++;
        }
        if(step==4) break;
    }
}

int main(void){
    int len, i=0, width, order=1;
    char data[SIZE]="202001010";
	len=strlen(data);
    width=4;
	if (len==1)
		plot2(4,0,0);
	else
	    square(data, width, &i, &order);
    return 0;
}