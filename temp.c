#include <stdio.h>
#include <string.h>

typedef struct cat {
    char name[10];
    void (*talk)(int money);
} cat_t;

void talkLarge(int money) {
    printf("LARGE %d\n", money);
}
void talkSmall(int money) {
    printf("SMALL %d\n", money);
}
void CatTalk(cat_t catX, int money) {
    catX.talk(money);
}
void test01() {
    cat_t cat001;
    strcpy(cat001.name, "Tom");
    cat001.talk = talkLarge;
    CatTalk(cat001, 1000);
    cat001.talk = talkSmall;
    CatTalk(cat001, 10);
}

void talkEnglish(char name[]) {
    printf("Hello! %s, ", name);
}
void talkDeutsch(char name[]) {
    printf("Hallo! %s, ", name);
}

void run02(void talk(char *), char name[]) {
    void (*f)(char *);
    talk(name);
    talk = talkEnglish;
    talk(name);
    f = talk;
    f(name);
}

int main() {
    run02(talkDeutsch, "John");
    return 0;
}