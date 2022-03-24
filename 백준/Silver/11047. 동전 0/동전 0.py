n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

cnt = 0
for x in coin[::-1]:
    while k >= x:
        cnt += k//x
        k = k%x
print(cnt)