import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n1):
	for n2 in range(1, N + 1):
		if adj[n1][n2] == 1 and visited[n2] == 0:
			visited[n2] = 1
			dfs(n2)


N, M = map(int, input().split())
adj = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):              # 간선
	u, v = map(int, input().split())
	adj[u][v] = 1
	adj[v][u] = 1

cnt = 0
visited = [0] * (N + 1)
for i in range(1, N + 1):
	if visited[i] == 0:         # 방문 안한 정점에서 dfs하여 연결 요소 모두 방문
		cnt += 1
		dfs(i)
print(cnt)