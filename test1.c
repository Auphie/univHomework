#include <stdio.h>
int main(void) {
    int state=0, input=0, score=0, i=0;
    for (i=0; i<5; i++) {
        scanf("%c%*c", &input);
        if (input != 'H') {
            state = (state <<((int)input-48)) | (1<<((int)input-49));
        } else {
           state = 0;
        }
    }
    state = state&7;

    printf("%d\n%d\n%d\n", state&1, (state>>1)&1, (state>>2)&1);
    return 0;
}
