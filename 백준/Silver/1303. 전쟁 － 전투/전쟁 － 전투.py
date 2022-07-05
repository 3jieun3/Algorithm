import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(r, c):
	global w_power, b_power, cnt
	visited[r][c] += 1
	cnt += 1
	for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
		nr, nc = r + dr, c + dc
		if 0 > nr or nr >= M or 0 > nc or nc >= N:
			continue
		if visited[nr][nc] == 0 and mmap[nr][nc] == mmap[r][c]:
			dfs(nr, nc)


N, M = map(int, input().split())
mmap = [input().rstrip() for _ in range(M)]
visited = [[0] * N for _ in range(M)]

w_power, b_power = 0, 0
for _r in range(M):
	for _c in range(N):
		if visited[_r][_c] == 0:
			cnt = 0        # 모인 병사 명수
			dfs(_r, _c)
			if mmap[_r][_c] == 'W':
				w_power += cnt ** 2
			else:
				b_power += cnt ** 2

print(w_power, b_power)