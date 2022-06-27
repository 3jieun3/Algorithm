import sys
from collections import deque
input = sys.stdin.readline

def bfs(st_user):
	while q:
		u = q.popleft()
		kb = kevin_bacon[u]         # st_user 로부터 u 까지의 단계
		for v in range(1, N + 1):
			if v == st_user:        # 본인 제외
				continue
			if friends[u][v] == 1 and kevin_bacon[v] == 0:      # u와 친구이고 st_user 로부터 단계 없는 사람
				q.append(v)
				kevin_bacon[v] = kb + 1

	return sum(kevin_bacon)


N, M = map(int, input().split())
friends = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
	a, b = map(int, input().split())
	friends[a][b] = 1
	friends[b][a] = 1

min_user, min_kevin = 0, 100

for user in range(1, N + 1):
	kevin_bacon = [0] * (N + 1)
	q = deque([user])
	# user 로부터 모든 사람까지의 단계
	ssum = bfs(user)
	# 케빈 베이컨 수 갱신
	if ssum < min_kevin:
		min_user = user
		min_kevin = ssum

print(min_user)