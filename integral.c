#include <stdio.h>
#include <stdlib.h>
#include <string.h>

double square(double x) { return x * x;}
double cube(double x) { return x * x * x;}
/* 計算f()在(x,y)間以n等份逼近的積分數值，使用梯形法 */
double integral(double (*f)(double), int n, double x, double y) {
    int i;
    double gap = (y - x) / n;
    double fy1 = (*f)(x);
    double fy2 = (*f)(x + gap);
    double area = 0;
    for (i = 0; i < n; i++) {
        area += (fy1 + fy2) * gap / 2;
        fy1 = fy2;
        fy2 = (*f)(x + gap * (i + 1));
    }
    return area;
}

int main() {
    char fun[100];
    int n;
    double x, y;
    double (*f)(double); // f: a pointer to function(double) returning double
        while (scanf("%99s",fun) != EOF) { // EOF定義於stdio.h內,一般為-1
        if (strcmp(fun,"square")==0) { f = square; } 
        else if (strcmp(fun,"cube")==0) { f = cube; } 
        else if (strcmp(fun,"end")==0) { break; } 
        else {
        printf("Unknown function\n");
        continue;
        }
    scanf("%d%lf%lf", &n, &x, &y);
    printf("Integral of %s from %lf to %lf is: %lf\n", fun, x, y, integral(f, n, x, y));
    }
    return 0;
}