#include <stdio.h>

int main(void) {
int pari, lesson[3][5];
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
lesson[2][4]=13;

/*    int lesson[3][3];
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            scanf("%d", &lesson[i][j]);
        }
    }
    printf("%d", lesson[0][2]);
*/
//for pair in range(0, len(schedule)-1):  # set length of pairs to pinch (classes -1)
for (int pair=0; pair<2; pair++) {
//    for i in lesson[pair][2:]:        # take target period from L to R to do pinch match
    for (int i=2; i<5; i++) {
//        for j in range(pair+1, len(lesson)):  # j is index of classes to do pair comparison
        for (int j=pair+1; j<3; j++) {
//            if lesson[i] in lesson[j][2:]:    # check i is in lesson[j]
            if(strcmp(lesson[i], s)==0){
                // Do your stuff
            }
                print('{0} and {1} confict on {2}'.format(lesson[pair][0],lesson[j][0], i))
        }
    }
}

    return 0;
}