import sys
input = sys.stdin.readline

def bfs():
	while q:
		r, c = q.pop(0)
		cnt = visited[r][c]
		if (r, c) == (N, M):    # 도착
			return cnt

		for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:   # 상하좌우
			nr = r + dr
			nc = c + dc
			if 1 > nr or nr > N or 1 > nc or nc > M:
				continue
			if maze[nr][nc] == 1 and visited[nr][nc] == 0:
				q.append((nr, nc))
				visited[nr][nc] = cnt + 1


N, M = map(int, input().split())
maze = [[0] * (M + 1)] + [[0] + list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * (M + 1) for _ in range(N + 1)]
q = [(1, 1)]
visited[1][1] = 1
print(bfs())