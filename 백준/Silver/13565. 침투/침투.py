import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(r, c):
	global rst
	visited[r][c] = 1
	if r == M - 1:      # inner side 도달시 종료
		rst = "YES"
		return

	for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
		nr, nc = r + dr, c + dc
		if 0 > nr or nr >= M or 0 > nc or nc >= N:
			continue
		if visited[nr][nc] == 0 and grid[nr][nc] == 0:
			dfs(nr, nc)
			if rst == "YES":
				return


M, N = map(int, input().split())
grid = [list(map(int, list(input().rstrip()))) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
rst = "NO"
# outer side (0행) 의 0에서 dfs
for j in range(N):
	if grid[0][j] == 0:
		visited = [[0] * N for _ in range(M)]
		dfs(0, j)
		if rst == "YES":
			break
print(rst)