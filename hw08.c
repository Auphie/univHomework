#include <stdio.h>
#include <stdlib.h>

void printMarks(int times, char mark){
    for (int i=0; i<times; i++){
        printf(" %c", mark);
    }
}

void to_rightTri(int n, int m){
    int i, times;
    for (i=1; i<=n+1; i++){
        times=m-abs(m-i);
        printMarks(times, '*');
        printf("\n");
    }
}

void to_leftTri(int n, int m){
    int i, dotTimes, asteriskTimes;
    for (i=1; i<n+1; i++){
        dotTimes = abs(m-i);
        asteriskTimes = m-abs(m-i);
        printMarks(dotTimes, '.');
        printMarks(asteriskTimes, '*');
        printf("\n");
    }
}

void to_dimond(int n, int m){
    int i, dotTimes, asteriskTimes;
    for (i=1; i<n+1; i++){
        dotTimes = abs(m-i);
        asteriskTimes = 2*(m-abs(m-i))-1;
        printMarks(dotTimes, '.');
        printMarks(asteriskTimes, '*');
        printf("\n");
    }
}

int main(){
    int story, medium, selectType;
    scanf("%d",&selectType);
    scanf("%d",&story);
    medium=story/2+1;
//    to_rightTri(story, medium);
    if (selectType==1){
        to_rightTri(story, medium);
    }
    else if (selectType==2){
        to_leftTri(story, medium);
    }
    else if (selectType==3){
        to_dimond(story, medium);
    }
    else {printf("input out of options");}
    return 0;
}