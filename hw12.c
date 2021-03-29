#include <stdio.h>

void scan_fraction(int *numerator, int *denominator) {
    char slash;
    int status; /* status code returned by scanf indicating number of valid values obtained */
    int error; 
    char discard; 
    do { 
        error = 0;
        printf("Enter a common fraction as two integers separated by a slash> ");
        status = scanf("%d%c%d",&numerator, slash, &denominator);
        if (status < 3) {
            error = 1;
            printf("Invalid-please read directions carefully\n");
        }
        else if (slash != '/') {
            error = 1;
            printf("Invalid-separate numerator and denominator");
            printf(" by a slash (/)\n");
        } else if (*denominator <= 0) {
            error = 1;
            printf("Invalid—denominator must be positive\n");
        }
        /* Discard extra input characters */
        do {
            scanf("%c", &discard);
        } while (discard != '\n');
    } while (error);
}