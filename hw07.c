#include <stdio.h>

float transValue(char card){
    switch(card){
        case 'A':
            return 1.0;
            break;
        case 'J':
            return 0.5;
            break;
        case 'Q':
            return 0.5;
            break;
        case 'K':
            return 0.5;
            break;
        case '1':
            return 10;
            break;
        default:
            return (float)card -'0';
    }
}

float call(){
    char face;
    float point;
    scanf(" %c", &face);
    point = transValue(face);
    return point;
}

float getNcard(int n){
    float pointSum, face;
    pointSum=0.0;
    for (int i=0; i<3; i++){
        face=call();
        pointSum+=face;
    }
    pointSum=(pointSum>10.5)?0:pointSum;
    return pointSum;
}

int main(){
    int cardNum;
    float resultA, resultB;
    char winner;
    cardNum=3;
    resultA=getNcard(cardNum);
    resultB=getNcard(cardNum);
    printf("%.1f\n%.1f\n",resultA,resultB);
    if (resultA>resultB) printf("A wins.\n");
    else if (resultA<resultB) printf("B wins.\n");
    else printf("It's a tie.\n");
    return 0;
}