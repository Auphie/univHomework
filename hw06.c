#include <stdio.h>

int main(){
    int inVoice, outVoice, localVoice, inText, outText, bestChoice;
    double minPrice, pA, pB, pC;
    inVoice=scanf("%d",&inVoice);
    outVoice=scanf("%d",&outVoice);
    localVoice=scanf("%d",&localVoice);
    inText=scanf("%d",&inText);
    outText=scanf("%d",&outText);
    pA = (inVoice*0.08)+(outVoice*0.1393)+(localVoice*0.1349)+(inText*1.1287)+(outText*1.4803);
    printf("pa_1%d\n", pA);
    pA = (183.0>pA)?183.0:pA;
    printf("pa_2%d\n", pA);
    bestChoice=183;
    pB = (inVoice*0.07)+(outVoice*0.1304)+(localVoice*0.1217)+(inText*1.1127)+(outText*1.2458);
    pB = (383.0>pB)?383.0:pB;
    bestChoice = (pB<pA)?383:bestChoice;
    pC = (inVoice*0.06)+(outVoice*0.1087)+(localVoice*0.1018)+(inText*0.9572)+(outText*1.1243);
    pC = (983.0>pC)?983.0:pC;
    bestChoice = (pC<pA && pC<pB)?983:bestChoice;
    printf("pA=%.1f,pB=%.1f,pC=%.1f\n", pA, pB, pC);
    printf("%d", bestChoice);
}