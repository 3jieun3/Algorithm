import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(M)]
# N개 이하 당첨된 것의 당첨 개수 저장
temp = []
for i in range(M):
	win, lose = cards[i]
	if win < N:
		temp.append(win)
# 당첨 개수 많은 것부터 M-1개이상 될때까지 비용 계산
ans = 0
temp.sort()
while len(temp) > 1:
	ans += N - temp.pop()
print(ans)