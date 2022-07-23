VOWELS = ['a', 'e', 'i', 'o', 'u']

def dfs(i, vowel_cnt, cons_cnt, pwd):
    if len(pwd) == L:                                   # 길이 L
        if vowel_cnt >= 1 and cons_cnt >= 2:    # 모음 자음 개수 체크
            passwords.append(pwd)
        return
    if i == C:
        return
    for j in range(i, C):                               # i 번째 이후의 문자들
        if chars[j] in VOWELS:
            dfs(j + 1, vowel_cnt + 1, cons_cnt, pwd + chars[j])
        else:
            dfs(j + 1, vowel_cnt, cons_cnt + 1, pwd + chars[j])


L, C = map(int, input().split())
chars = sorted(input().split())     # 사전 순 정렬
passwords = []
dfs(0, 0, 0, '')
if passwords:
    print(*passwords, sep="\n")