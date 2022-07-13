import sys
from collections import deque
input = sys.stdin.readline

def bfs():
	global rst
	while q:
		r, c = q.popleft()
		val = mmap[r][c]
		if val == -1:
			return "HaruHaru"
		for dr, dc in [(1, 0), (0, 1)]:
			nr = r + dr * val
			nc = c + dc * val
			if 0 > nr or nr >= N or 0 > nc or nc >= N:
				continue
			if visited[nr][nc] == 0:
				q.append((nr, nc))
				visited[nr][nc] = 1
	return "Hing"


N = int(input())
mmap = [list(map(int, input().split())) for _ in range(N)]
q = deque([(0, 0)])
visited = [[0] * N for _ in range(N)]
print(bfs())