import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(r, c):
	visited[r][c] = 1
	for k in range(8):
		nr = r + dr[k]
		nc = c + dc[k]
		if 0 > nr or nr >= M or 0 > nc or nc >= N:
			continue
		if arr[nr][nc] and visited[nr][nc] == 0:
			dfs(nr, nc)


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
cnt = 0
for i in range(M):
	for j in range(N):
		# 새로운 글자 시작점에서 dfs
		if arr[i][j] and visited[i][j] == 0:
			dfs(i, j)
			cnt += 1

print(cnt)