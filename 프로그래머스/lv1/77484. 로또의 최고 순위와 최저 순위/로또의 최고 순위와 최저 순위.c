#include <stdio.h>
#include <stdlib.h>

int* solution(int lottos[], size_t lottos_len, int win_nums[], size_t win_nums_len) {
    
    int* answer = (int*)malloc(sizeof(int)*2);
    
    int rank[7] = {6, 6, 5, 4, 3, 2, 1};
    
    int zero = 0;
    for(int i=0; i<6; i++) {
        if (lottos[i] == 0) zero++;
    }
    
    int same = 0;
    for (int i=0; i<6; i++){
        for (int j=0; j<6; j++){
            if (win_nums[i] == lottos[j]) same++;
        }
    }
    
    answer[0] = rank[same+zero];
    answer[1] = rank[same];
    
    return answer;
}