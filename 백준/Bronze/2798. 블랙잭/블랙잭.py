n, m = map(int, input().split())
card = list(map(int, input().split()))

rst = 0
tmp = 0
# 모든 조합 경우의 수를 다 따져봄 : 브루트포스
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            tmp = card[i] + card[j] + card[k]
            if tmp <= m:
                if tmp > rst: 
                    rst = tmp
print(rst)