#include<stdio.h>           /*引用头文件*/
int gys(int x,int y) {
    return y?gys(y,x%y):x;  /*递归调用gys，返回最大公约数*/
}

int gbs(int x,int y) {
    return x/gys(x,y)*y;
}

void yuefen(int fz,int fm) {
    int s=gys(fz,fm);
    fz/=s;
    fm/=s;
    printf("the result is %d/%d\n",fz,fm);
}

void add(int a,int b,int c,int d) {
    int u1,u2,v=gbs(b,d),fz1,fm1;
    u1=v/b*a;
    u2=v/d*c;
    fz1=u1+u2;
    fm1=v;
    yuefen(fz1,fm1);
}

void mul(int a,int b,int c,int d) {
    int u1,u2;
    u1=a*c;
    u2=b*d;
    yuefen(u1,u2);
}

void sub(int a,int b,int c,int d){
    int u1,u2,v=gbs(b,d),fz1,fm1;
    u1=v/b*a;
    u2=v/d*c;
    fz1=u1-u2;
    fm1=v;
    yuefen(fz1,fm1);
}

void div(int a,int b,int c,int d){
    int u1,u2;
    u1=a*d;
    u2=b*c;
    yuefen(u1,u2);
}
int main(void){
    char op;
    char a1,a2;
    int a,b,c,d;
    printf("输入两个分数的运算：\n");
    scanf("%ld%c%ld%c%ld%c%ld",&a,&a1,&b,&op,&c,&a2,&d);
    if(a1=='/'&&a2=='/'){
        switch(op){
            case '+':add(a,b,c,d);break;    /*调用加法函数*/
            case '*':mul(a,b,c,d);break;    /*调用乘法函数*/
            case '-':sub(a,b,c,d);break;    /*调用减法函数*/
            case '/':div(a,b,c,d);break;    /*调用除法函数*/
        }
    }
    else printf("输入的格式不对\n");
    return 0;
}