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
    int remainder=0, quotient = 0, GCD=gcd(up,down);
    up/=GCD;
    down/=GCD;
    quotient = up/down;
    remainder = up%down;
    if (remainder!=0){
        if (abs(quotient)>0){
            up = up - quotient*down;
            if (up<0 || down <0)
                printf("-%d(%d/%d)",quotient, abs(up),abs(down));
            else
                printf("+%d(%d/%d)",quotient, up, down);
        }
        else if (up<0 || down <0)
            printf("-%d/%d", abs(up),abs(down));
        else
            printf("+%d/%d", up, down);
    }
    else if (quotient>0)
        printf("+%d",quotient);
    else if (quotient<0)
        printf("%d",quotient);
}

void reduction2(int up,int down) {
    int remainder=0, quotient = 0, GCD=gcd(up,down);
    up/=GCD;
    down/=GCD;
    quotient = up/down;
    remainder = up%down;
    if (remainder!=0){
        if (abs(quotient)>0){
            up = up - quotient*down;
            if (up<0 || down <0)
                printf("-%d(%d/%d)",abs(quotient), abs(up),abs(down));
            else
                printf("%d(%d/%d)",abs(quotient), up, down);
        }
        else printf("%d/%d",up, down);
    }
    else if (remainder==0){
        if (abs(quotient)>1)
            printf("%d",quotient);
        else if (quotient==-1)
            printf("-");
    }
    else {
        if (up<0 || down <0)
            printf("-%d/%d", abs(up),abs(down));
        else
            printf("+%d/%d", up, down);
    }
}

void sub(int up1,int down1,int up2,int down2) {
    int num1, num2, LCM=lcm(down1,down2), up, down;
    up = up1*down2 - up2*down1;
    down = LCM;
    reduction(up,down);
}

int main(void) {
    int x1, y1, x2, y2, m_up, m_down, b_up, b_down;
    scanf("%d, %d", &x1, &y1);
    scanf("%d, %d", &x2, &y2);
    m_up = y2-y1;
    m_down = x2-x1;
    printf("y=");
    reduction2(m_up, m_down);
    printf("x");
    sub(y1 ,1 , m_up*x1, m_down);
    printf("\n");
    return 0;
}