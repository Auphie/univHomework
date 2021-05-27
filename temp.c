#include <stdio.h>
#include <stdlib.h>

typedef struct student_s {
    const char name[8];
    int student_id, scorePG, scoreCI;
    double scoreAvg;
} student_t;

void Write(char fileName[], student_t s) {
    FILE * fp;
    long lSize;
    fp = fopen (fileName, "ab+");
    fwrite(&s, sizeof(student_t), 1, fp);
    fclose(fp);
}

void Print(char fileName[]){
    FILE * fp;
    int i;
    student_t s;
    long lSize;
    fp = fopen (fileName, "rb");
    fseek(fp, 0, SEEK_END);
    lSize=ftell(fp);
    rewind(fp);
//    fread(&s1, lSize, 1, fp);
    fread(s, lSize, 1, fp); //讀檔案
    printf("name=%s, ID=%d, avg score=%.2f\n", s.name, s.student_id, (s.scorePG+s.scoreCI)/2.0);
    fclose(fp);
}

int main(void) {
    student_t s1={"John", 109590010, 100, 90};
    student_t s2={"Tom", 109590011, 90, 80};
    student_t s3={"Ken", 109590012, 80, 95};
    Write("score.txt", s1);
    Write("score.txt", s2);
    Write("score.txt", s3);
    Print("score.txt");
    return 0;
}