#include <stdio.h>
#include <string.h>

void numCmp(char *s1, char *s2) {
   int r = strcmp(s1,s2);
   printf("result=%d\n", r); //= -1 (or not 0) if not the same
   r = strncmp(s1,s2,4);
   printf("result=%d\n", r); //= 0 because both are fully the same
}

int myNumCmp(char *s1, char *s2) {
    if (strlen(s1)>strlen(s2))
        return 1;
    else if (strlen(s1)<strlen(s2))
        return -1;
    else {
        for (;(*s1!='\0')&&(*s2!='\0');s1++, s2++) {
            if (*s1>*s2) return 1;
            else if (*s1<*s2) return -1;
        }
    }
    return 0;
}

void split(char* str, char* delim) {
    char* pch;
    pch = strtok(str,delim);
    while (pch != NULL) {
        printf("%s-",pch);
        pch = strtok (NULL, delim);
    }
}

int main(void){
    char str1[10]="4234";
    char str2[10]="1234";
    char str3[10]="12345";
    char str4[]="00:22:33:4B:55:5A";
    char *delim = ":";
/*
    printf("%d\n",strcmp(str1, str3));  //= 1 (4>1)
    printf("%d\n",strcmp(str2, str3));  //= -1 (len 4<5 digits)
    printf("%d\n",strncmp(str2, str3, 4)); //=0 (1234=1234)
    numCmp(str1, str2);
    printf("%d",myNumCmp(str1, str2));
    split(str4, delim);
*/
    char* strcat1=strcat(str1, str2);
    printf("strcat1=%s\n", strcat1);
    char* strcat2=strncat(str1, str2, sizeof(str1)-strlen(str1)-1);
    strcat2[sizeof(strcat2)]='\0';
    printf("strcat2=%s\n", strcat2);

    return 0;
}