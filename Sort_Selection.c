#include <stdio.h>
#define SWAP(x,y) {int t; t = x; x = y; y = t;}

void swap(int *xp, int *yp){
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

/*  arr = 64 25 12 22 11
        ['11' 25 12 22 '64']    from [0] to [n], find the min, swap [0] & [i].
        11 ['12' '25' 22 64]    from [1] to [n], find the min, swap [1] & [i].
        11 12 ['22' '25' 64]    from [2] to [n], find the min, swap [2] & [i].
        11 12 22 ["25" "64"]    from [3] to [n], find the min, swap [3] & [i].
*/
void selectSort(int arr[], int n) {
    int i, j, min_idx=0;
    for (i = 0; i < n-1; i++){
        min_idx = i;
        for (j = i+1; j < n; j++)
          if (arr[j] < arr[min_idx])
            min_idx = j;
        SWAP(arr[i], arr[min_idx]);
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