#include <stdio.h>
#include <math.h>

double square(double x) { return x * x;} 
double cube(double x) { return x * x * x;}

double integral(double (*f)(double), int n, double x, double y) {
    int i;
    double gap = (y - x) / n;
    double fy1 = (*f)(x);
    double fy2 = (*f)(x + gap);
    double area = 0;
    for (i = 0; i < n; i++) {
        area += (fy1 + fy2) * gap / 2; // 使用梯形面積公式
        fy1 = fy2;
        fy2 = (*f)(x + gap * (i + 1)); //下底
    }
    return area;
}

double integral(double (*f)(double), int n, double x, double y) {
    int i;
    double area = ((*f)(x) + (*f)(y)) / 2.0L;
    double gap = (y - x) / n;
    double next = x;
    for (i = 1; i < n; i++) {
        area += (*f)(next += gap);
    }
    return area * gap;
}

int main() {
    char fun[100];
    int n;
    double x, y;
    double (*f)(double); // f: a pointer to function(double) returning double
    while (scanf("%99s",fun) != EOF) { // EOF定義於stdio.h內,一般為-1
        if (strcmp(fun,"square")==0) { f = square; } 
        else if (strcmp(fun,"cube")==0) { f = cube; } 
        else if (strcmp(fun,"sqrt")==0) { f = sqrt; } // sqrt is defined in math.h
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