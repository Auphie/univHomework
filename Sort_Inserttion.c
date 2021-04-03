#include <stdio.h>

/*  arr = 64 25 12 22 11    
        [64] "25" 12 22 11  i=1 (key=25), [64]>25 so 64 = arr[i]
        [25 64] 12 22 11         & insert key into smallest[<i].
        [25 64] "12" 22 11  i=2 (key=12), [25 64]>12 so shift elms of scope >>
        [12 25 64] 22 11         & insert key to the smallest position arr[0]
        [12 25 64] "22" 11  i=3 (key=22), [25 64]>22 so shift >>
        [12 22 25 64] 11         & insert key to the smallest position arr[1]
        [12 22 25 64] "11"  i=4 (key=11), [12 22 25 64]>11 so shift >>
        [11 12 22 25 64]         & insert key to the smallest position arr[0]
*/
void insertionSort(int arr[], int n){
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;    //scope from arr[i-1] to arr[0] decending check
        while (j >= 0 && arr[j] > key) {    //when elms of scope > key
            arr[j + 1] = arr[j];            //shift srr[j] >>
            j = j - 1;        //iterate decending to find the smallest position
        }                     //from arr[0] to arr[j] until arr[j]<key
        arr[j + 1] = key;   //insert key into the smallest position of scope
    }
}
 
void printArray(int arr[], int n){
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}
 
int main(){
    int arr[] = { 64, 25, 12, 22, 11 };
    int n = sizeof(arr) / sizeof(arr[0]);
    insertionSort(arr, n);
    printArray(arr, n); 
    return 0;
}