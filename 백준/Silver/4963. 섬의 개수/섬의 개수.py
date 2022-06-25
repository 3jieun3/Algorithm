import sys
input = sys.stdin.readline

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs():
	island = 0
	# 새로운 섬 찾기
	for _r in range(h):
		for _c in range(w):
			if visited[_r][_c] == 0 and mmap[_r][_c] == 1:
				q.append((_r, _c))
				visited[_r][_c] = 1
				island += 1
				# 섬 영역 탐색하고 방문 처리
				while q:
					r, c = q.pop(0)
					for k in range(8):
						nr = r + dr[k]
						nc = c + dc[k]
						if 0 > nr or nr >= h or 0 > nc or nc >= w:
							continue
						if mmap[nr][nc] == 1 and visited[nr][nc] == 0:
							q.append((nr, nc))
							visited[nr][nc] = 1
	return island


results = []
while True:
	w, h = map(int, input().split())
	if w == 0 and h == 0:
		break
	mmap = [list(map(int, input().split())) for _ in range(h)]  # 1 땅, 0 바다
	visited = [[0] * w for _ in range(h)]
	q = []
	results.append(bfs())

print(*results, sep="\n")