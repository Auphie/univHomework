#include <stdio.h>
#include <string.h>
#include<stdlib.h>

void swap1(char *str1, char *str2) {
   char *temp = str1;
   str1 = str2;
   str2 = temp;
}

//This method cannot be applied if strings are stored using character arrays.
void swap2(char **str1_ptr, char **str2_ptr) {
    char *temp = *str1_ptr;
    *str1_ptr = *str2_ptr;
    *str2_ptr = temp;
} 

//This method can apply to array
void swap3(char *str1, char *str2) {
    char *temp = (char *)malloc((strlen(str1) + 1) * sizeof(char));
    strcpy(temp, str1);
    strcpy(str1, str2);
    strcpy(str2, temp);
    free(temp);
}

int main() {
   char *str1 = "geeks";
   char *str2 = "forgeeks";
   //str3&4 are array, so can't apply to swap2(** method)
   char str3[] = "geeks"; // = {"geeks"};
   char str4[] = "forgeeks"; // = {"forgeeks"};
   
   printf("0. str1=\"%s\" & str2=\"%s\"\n", str1, str2);
/*
   swap1(str1, str2);
   printf("1. str1=\"%s\" & str2=\"%s\" has no swap\n", str1, str2);

   swap2(&str1, &str2);
   printf("2. str1=\"%s\" & str2=\"%s\" has swapped!\n", str1, str2);
*/
   swap3(str3, str4);
   printf("3. str3=\"%s\" & str4=\"%s\" by swapping arrays\n" , str3, str4);

   return 0;
}