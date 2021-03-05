#include <stdio.h>

int main(){
    int inVoice, outVoice, localVoice, inText, outText, bestChoice;
    int minPrice, pA, pB, pC;
    inVoice=300;
    outVoice=300;
    localVoice=300;
    inText=300;
    outText=300;
    pA = (inVoice*0.08)+(outVoice*0.1393)+(localVoice*0.1349)+(inText*1.1287)+(outText*1.4803);
    printf("%d", pA);
}
