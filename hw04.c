#include <stdio.h>
#define PI 3.14159

void main(void) {
float radius, perimeter, area;

scanf("%f",&radius);

perimeter = 2*radius*PI;
area = radius*radius*PI;
printf("%.3f\n",area);
printf("%.3f\n",perimeter);
}
