#include<stdio.h>
#include<string.h>
#define SIZE 20

int square(char data[SIZE], int width, int* i){
    int total=0, step=0, len=strlen(data);
    while((*i)<len){
        step++;
        if(data[*i]=='2'){
            (*i)++;
            total = total+ square(data, width/2, i);
        }
        else if(data[*i]=='1'){
            total = total+(width*width);
            (*i)++;
        }
        else if(data[*i]=='0'){
            (*i)++;
        }
        if(step==4) break;
    }
    return total;
}

void plot(int x, int y){
    
}

int main(void){
    int len, i=0, width, total=0;
    char data[SIZE]="202001010";
    width=4;
    total = square(data, width, &i);
    printf("%d\n",total);
    //scanf("%s",&data); scanf("%d",&n);length = strlen(data); 
    //printf("%d",square(data ,length ,n ,&i)); 
/*
    printf("%d\n",square("2020020100010" ,13 ,8 ,&i));i=0;//17 
    printf("%d\n",square("2020020100010" ,13 ,4 ,&i));i=0;//7
    printf("%d\n",square("2020010120110", 13, 8, &i));i=0;//28
    printf("%d\n",square("2021000200110", 13, 4, &i));i=0;//3
*/
    return 0;
}