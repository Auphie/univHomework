#include <stdio.h>

int main(void) {
int pari, lesson[3][5];
/*
lesson[0][0]=1001;
lesson[0][1]=3;
lesson[0][2]=11;
lesson[0][3]=12;
lesson[0][4]=13;
lesson[1][0]=1002;
lesson[1][1]=3;
lesson[1][2]=21;
lesson[1][3]=22;
lesson[1][4]=23;
lesson[2][0]=1003;
lesson[2][1]=3;
lesson[2][2]=31;
lesson[2][3]=32;
lesson[2][4]=23;
*/
for (int i=0; i<3; i++) {
    for (int j=0; j<5; j++) {
        scanf("%d", &lesson[i][j]);
    }
}

for (int pair=0; pair<2; pair++) {
    for (int i=2; i<5; i++) {
        for (int j=pair+1; j<3; j++) {
            if(lesson[j][i] == lesson[pair][i]){
                printf("%d and %d conflict on %d", lesson[pair][0],lesson[j][0],lesson[j][i]);
            }
        }
    }
}
    return 0;
}