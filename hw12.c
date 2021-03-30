#include <stdio.h>
#include <stdlib.h>

int gcd(int up, int down) {
    if (down !=0)
        return gcd(down,up%down);
    else
        return up; 
}

int lcm(int up,int down) {
    return up/gcd(up,down)*down;
}

void reduction(int up,int down) {
    int quotient = 0, GCD=gcd(up,down);
    up/=GCD;
    down/=GCD;
    quotient = up/down;
    if (up<0 || down <0)
        printf("the result is -%d/%d\n",abs(up),abs(down));
    else
        printf("the result is %d/%d\n",up,down);
}

void add(int up1,int down1,int up2,int down2) {
    int num1, num2, LCM=lcm(down1,down2), up, down;
    num1=LCM/down1*up1;
    num2=LCM/down2*up2;
    up=num1+num2;
    down=LCM;
    reduction(up, down);
}

void sub(int up1,int down1,int up2,int down2) {
    int num1, num2, LCM=lcm(down1,down2), up, down;
    num1=LCM/down1*up1;
    num2=LCM/down2*up2;
    up=num1-num2;
    down=LCM;
    reduction(up,down);
}

void mul(int up1,int down1,int up2,int down2) {
    int up, down;
    up=up1*up2;
    down=down1*down2;
    reduction(up,down);
}

void div(int up1,int down1,int up2,int down2) {
    int up, down;
    up=up1*down2;
    down=up2*down1;
    reduction(up,down);
}

int main(void) {
    int up1, up2, down1, down2;
    char slash1, slash2, op, next='y';
    while (next != 'n') {
        scanf("%d%c%d", &up1, &slash1, &down1);
        scanf("%d%c%d", &up2, &slash2, &down2);
        scanf(" %c", &op);
        scanf(" %c", &next);
        if (slash1 != '/' && slash2 != '/') 
            printf("ERROR\n");
        else if (down1==0 || down2==0)
            printf("ERROR\n");
        else {
            switch(op) {
                case '+':add(up1,down1,up2,down2);break;
                case '*':mul(up1,down1,up2,down2);break;
                case '-':sub(up1,down1,up2,down2);break;
                case '/':div(up1,down1,up2,down2);break;
            }
        }
    }
    return 0;
}