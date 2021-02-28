#include <stdio.h>
#include <math.h>
void main(void) {
int hour1, hour2, hourlyPay, wage, minWage;
float tax, insurance, finalIncome;

//scanf("%d",&a);
scanf("%d",&hour1);
scanf("%d",&hour2);
scanf("%d",&hourlyPay);
scanf("%d",&minWage);

wage = (hour1+hour2)*hourlyPay;
insurance = minWage * 0.05;
tax = wage * 0.08;
finalIncome = wage-insurance-tax;

printf("%.1f\n",finalIncome);
printf("%.1f\n",insurance);
printf("%.1f",tax);
}
