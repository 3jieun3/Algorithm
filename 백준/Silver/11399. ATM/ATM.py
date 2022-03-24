n = int(input())
p = [0] + list(map(int, input().split()))
# 최소시간 = 적게 걸리는 순서로
p.sort()
need = [0]
for i in range(1, n+1):
    need.append(need[i-1]+p[i])
print(sum(need))