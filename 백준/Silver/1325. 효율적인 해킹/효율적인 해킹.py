import sys
from collections import deque
input = sys.stdin.readline

def bfs():
	global mx_cnt

	for _v in range(1, N + 1):
		q.append(_v)                # 각 컴퓨터에서 시작
		visited = [0] * (N + 1)     # 방문 처리 초기화
		visited[_v] = 1
		cnt = 1
		while q:
			v = q.popleft()
			for w in computers[v]:  # w 가 v 를 신뢰
				if visited[w] == 0:
					q.append(w)
					cnt += 1
					visited[w] = 1

		hacked_counts[_v] = cnt     # _v 에서 시작했을 때 해킹 개수
		if mx_cnt < cnt:            # 최대 해킹 개수 갱신
			mx_cnt = cnt


N, M = map(int, input().split())
computers = [[] for _ in range(N + 1)]
for _ in range(M):
	a, b = map(int, input().split())            # a가 b를 신뢰 = b -> a 방향으로 인접
	computers[b].append(a)

q = deque()
hacked_counts = [0] * (N + 1)
mx_cnt = 0
bfs()

tmp = []
for i in range(1, N + 1):
	if hacked_counts[i] == mx_cnt:
		tmp.append(i)
print(*tmp)