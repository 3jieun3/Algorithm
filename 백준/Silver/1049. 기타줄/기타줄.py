import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
pack_price, one_price = 1000, 1000
for _ in range(M):
    a, b = map(int, input().split())
    pack_price = min(pack_price, a)
    one_price = min(one_price, b)

q, r = N // 6, N % 6
total = 0

if pack_price < one_price * 6:     # 패키지 가격이 유리
    total += pack_price * q
else:
    total += one_price * 6 * q
    
if pack_price < one_price * r:
    total += pack_price
else:
    total += one_price * r
    
print(total)