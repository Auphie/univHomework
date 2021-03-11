#include <stdio.h>

int main(void) {
    int courseN1, courseN2, courseN3, class1, class2, class3;

    scanf("%d", &class1);
    scanf("%d", &courseN1);
    int lesson1[courseN1];
    lesson1[0]=class1;
    for (int i=1; i<=courseN1; i++) 
        scanf("%d", &lesson1[i]);

    scanf("%d", &class2);
    scanf("%d", &courseN2);
    int lesson2[courseN2];
    lesson2[0]=class2;
    for (int i=1; i<=courseN2; i++) 
        scanf("%d", &lesson2[i]);

    scanf("%d", &class3);
    scanf("%d", &courseN3);
    int lesson3[courseN3];
    lesson3[0]=class3;
    for (int i=1; i<=courseN3; i++) 
        scanf("%d", &lesson3[i]);

    for (int i=1; i<courseN1+1; i++) {
        for (int j=1; j<courseN2+1; j++) {
            if(lesson1[i] == lesson2[j]){
                printf("%d and %d conflict on %d\n", lesson1[0],lesson2[0],lesson1[i]);
            }
        }
    }

    for (int i=1; i<courseN1+1; i++) {
        for (int j=1; j<courseN3+1; j++) {
            if(lesson1[i] == lesson3[j]){
                printf("%d and %d conflict on %d", lesson1[0],lesson3[0],lesson1[i]);
            }
        }
    }

    for (int i=1; i<courseN2+1; i++) {
        for (int j=1; j<courseN3+1; j++) {
            if(lesson2[i] == lesson3[j]){
                printf("%d and %d conflict on %d", lesson2[0],lesson3[0],lesson2[i]);
            }
        }
    }

    return 0;
}