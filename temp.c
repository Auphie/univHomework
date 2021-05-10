#include <stdio.h>
#include <string.h>
void check (char *a, char *b, int (*p)(const char*, const char*)) {
    if (!(*p) (a,b)) printf("equal");
    else printf("not equal");
}
int main(void) {
    char s1[80], s2[80];
    int (*p)(const char*, const char*)=strcmp;
    gets(s1);
    gets(s2);
    check(s1, s2, p);
}