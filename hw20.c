#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* replaceWord(const char* s, const char* oldW, const char* newW){
    char* result;
    int i, cnt = 0;
    int newWlen = strlen(newW);
    int oldWlen = strlen(oldW);
  
    // Counting the number of times old word
    // occur in the string
    for (i = 0; s[i] != '\0'; i++) {
        if (strstr(&s[i], oldW) == &s[i]) {
            cnt++;
            // Jumping to index after the old word.
            i += oldWlen - 1;
        }
    }
    // Making new string of enough length
    result = (char*)malloc(i + cnt * (newWlen - oldWlen) + 1);
  
    i = 0;
    while (*s) {
        // compare the substring with the result
        if (strstr(s, oldW) == s) {
            strcpy(&result[i], newW);
            i += newWlen;
            s += oldWlen;
        }
        else
            result[i++] = *s++;
    }
  
    result[i] = '\0';
    return result;
}
  
void split(char *arr, char* str, char* delim) {
   char *s = strtok(str, delim);
   int s_count=0;

   while(s != NULL) {
     *arr++=s;
     s = strtok(NULL, delim);
   }

   for(int x=0;x<s_count;x++) //驗收成果
      printf("%d %s\n",x,arr[x]);
}

int wordCounts(char* str, char* delim) {
    int i, counts=1, size=strlen(str);
    for (i=0; i<size; i++){
        if (str[i]==' ')
            counts+=1;
    }
    return counts;
}


int main(void){
    int wordCount=0;
    char str[] = "Can you can a can as a canner can can a can";
    char c[] = "can";
    char d[] = "ban"; 
    char delim=' ';
    char* result = NULL;
    wordCount=wordCounts(str, &delim);
    char *arr[14];
    result = replaceWord(str, c, d);
//    printf("New String: %s\n", result);
    split(arr, str, &delim);

    free(result);
    return 0;
}