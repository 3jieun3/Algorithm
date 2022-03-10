# 완탐) 높이의 범위가 정해져 있어서 257가지(0~256)의 시간을 다 확인 
import sys
input = sys.stdin.readline
from collections import Counter

n, m, b = map(int, input().split())
ground = []
ans = [100000000000000, 0]
for i in range(n):
    ground += map(int, input().split())

info = dict(Counter(ground)) # {높이 : 개수}
_sum = sum(ground)

for h in range(257):
    # 만들 높이의 총 높이 <= 현재 총 높이 + 인벤토리 여분 일때만 가능
    if h*n*m <= _sum + b:
        time = 0
        for key in info:
            if key < h:
                time += (h - key) * info[key]
            elif key > h:
                time += (key - h) * 2 * info[key]
        if time <= ans[0]:
            ans[0] = time
            ans[1] = h

print(ans[0], ans[1])