#include <stdio.h>
#define SWAP(x,y) {int t; t = x; x = y; y = t;}

int getMinIndex(int d[], int left, int right) {
  int i=0, minIndex = left;
  for ((i=left+1); i<right; i++) {
    if (d[i]<d[minIndex])
        minIndex=i;
  }
  return minIndex;
}

void selectSort(int arr[], int n) {
  int i=0, index=0;
  for (i=0; i<n; i++) {
    index = getMinIndex(arr, i, n);
    SWAP(arr[i], arr[index]);
  }
}

void printArray(int arr[], int size){
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main(void){
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr)/sizeof(arr[0]);
    selectSort(arr, n);
    printf("Sorted array: \n");
    printArray(arr, n);
    return 0;
}