
#include <stdio.h>
#include <math.h>
void main(void) {
int a, b, c;
float x1, x2;

scanf("%d",&a);
scanf("%d",&b);
scanf("%d",&c);

x1 = ((-b)+sqrt(b*b-4.0*a*c))/(2.0*a);
x2 = ((-b)-sqrt(b*b-4.0*a*c))/(2.0*a);

printf("%.1f\n",x1);
printf("%.1f",x2);
}
