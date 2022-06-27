import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
	for _r in range(M):
		for _c in range(N):
			if visited[_r][_c] == 0 and grid[_r][_c] == 0:
				q.append((_r, _c))
				visited[_r][_c] = 1
				size = 1
				while q:
					r, c = q.pop(0)
					for k in range(4):
						nr = r + dr[k]
						nc = c + dc[k]
						if 0 > nr or nr >= M or 0 > nc or nc >= N:
							continue
						if grid[nr][nc] == 0 and visited[nr][nc] == 0:
							q.append((nr, nc))
							visited[nr][nc] = 1
							size += 1
				areas.append(size)


M, N, K = map(int, input().split())     # M: 행, N: 열
arr = [list(map(int, input().split())) for _ in range(K)]

# 직사각형 채우기 (문제를 x축 대칭 시킴)
grid = [[0] * N for _ in range(M)]
for lc, lr, rc, rr in arr:  # 왼쪽 위 (열, 행), 오른쪽 아래 (열, 행)
	for i in range(lr, rr):
		for j in range(lc, rc):
			grid[i][j] = 1

# 분리 영역 bfs
visited = [[0] * N for _ in range(M)]
areas = []
q = []
bfs()

areas.sort()
print(len(areas))
print(*areas)