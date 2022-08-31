import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    global max_word
    if cnt <= K:
        word_cnt = 0
        for word in new_words:
            flag = True
            for w in word:
                if alpha[ord(w) - ord('a')] == 0:
                    flag = False
                    break
            if flag:
                word_cnt += 1

        if max_word < word_cnt:
            max_word = word_cnt

    if cnt == K or idx == 26:
        return

    for j in range(idx, 26):
        if alpha[j] == 0:
            alpha[j] = 1
            dfs(j + 1, cnt + 1)
            alpha[j] = 0


N, K = map(int, input().split())
new_words = [input().lstrip('anta').rstrip('tica\n') for _ in range(N)]

alpha = [-1] * 26       # -1:배울 필요 없음 / 0:배워야함 / 1:배움
for c in ['a', 'n', 't', 'i', 'c']:
    alpha[ord(c) - ord('a')] = 1

for wd in new_words:
    for i in range(len(wd)):
        if alpha[ord(wd[i]) - ord('a')] == -1:
            alpha[ord(wd[i]) - ord('a')] = 0

max_word = 0
dfs(0, 5)
print(max_word)
