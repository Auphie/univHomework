#include <stdio.h>
#define PI 3.14159

void main(void) {
    int firstBase=0, secondBase=0, thirdBase=0;
    int a=1,b=1,c=0,d=0,e=1;

    int state=0, input=0, score=0;
    scanf("%d", &input);
    state = (state <<input) | (1<<(input-1));
    state = state&7;
    scanf("%d", &input);
    state = (state <<input) | (1<<(input-1));
    state = state&7;
    scanf("%d", &input);
    state = (state <<input) | (1<<(input-1));
    state = state&7;
    printf("%d %d %d\n", state&1, (state>>1)&1, (state>>2)&1);
    return 0;
}
