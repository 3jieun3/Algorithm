import sys
input = sys.stdin.readline

def bfs():
	global paint_cnt, max_size
	for _r in range(n):
		for _c in range(m):
			# 각 그림마다 bfs
			if visited[_r][_c] == 0 and paint[_r][_c] == 1:
				q.append((_r, _c))
				visited[_r][_c] = 1
				paint_cnt += 1      # 그림 개수 증가
				size = 1            # 각 그림 넓이
				while q:
					r, c = q.pop(0)
					for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
						nr = r + dr
						nc = c + dc
						if 0 > nr or nr >= n or 0 > nc or nc >= m:
							continue
						if visited[nr][nc] == 0 and paint[nr][nc] == 1:
							q.append((nr, nc))
							visited[nr][nc] = 1
							size += 1
				if max_size < size:     # 최대 넓이 갱신
					max_size = size


n, m = map(int, input().split())
paint = [list(map(int, input().split())) for _ in range(n)]
q = []
visited = [[0] * m for _ in range(n)]
paint_cnt = 0
max_size = 0
bfs()
print(paint_cnt)
print(max_size)