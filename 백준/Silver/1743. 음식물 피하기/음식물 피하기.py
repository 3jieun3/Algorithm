import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(r, c):
	global size
	visited[r][c] = 1
	size += 1
	for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
		nr, nc = r + dr, c + dc
		if 1 > nr or nr > N or 1 > nc or nc > M:
			continue
		if visited[nr][nc] == 0 and mmap[nr][nc] == 1:
			dfs(nr, nc)


N, M, K = map(int, input().split())
mmap = [[0] * (M + 1) for _ in range(N + 1)]
for _ in range(K):
	i, j = map(int, input().split())
	mmap[i][j] = 1        # 음식물 위치 저장

mx_size = 0
visited = [[0] * (M + 1) for _ in range(N + 1)]
for _r in range(1, N + 1):
	for _c in range(1, M + 1):
		if visited[_r][_c] == 0 and mmap[_r][_c] == 1:  # 음식물 위치 찾아 dfs
			size = 0        # 사이즈 초기화
			dfs(_r, _c)
			if mx_size < size:  # 최대 사이즈 갱신
				mx_size = size

print(mx_size)