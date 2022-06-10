#include <stdio.h>

int main(void) {
    int a;
    int b;
    scanf("%d %d", &a, &b);
    
    for(int m=0; m < b; m++){
        for(int n=0; n < a; n++)
            printf("*");
        printf("\n");
    }
    return 0;
}