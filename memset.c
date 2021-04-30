#include<stdio.h>
#include<string.h>
#define SIZE 20

int main(void) {
   char s2[][20] = {"Hi", "Hello", "Good"};
   printf("%s\n", memset(s2, '#', 22));
   printf("%s\n", s2[0]);  //######################llo (22# in line)
                           /*the first 20 # occupies all s2[0]
                           without \0, so it continues to print
                           ##llo until \0 has met. */
   printf("%s\n", s2[1]);  //##llo
   printf("%s\n", s2[2]);  //Good
return 0;
}
