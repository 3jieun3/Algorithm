import sys
input = sys.stdin.readline

def bfs(visited):
	while q:
		r, c = q.pop(0)
		for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			nr = r + dr
			nc = c + dc
			if 0 > nr or nr >= N or 0 > nc or nc >= N:
				continue
			# 아직 가라앉지 않았고 높이가 h 이하인 경우 이제 가라앉아야해
			if visited[nr][nc] == 0 and sink[nr][nc] == 0:
				q.append((nr, nc))
				visited[nr][nc] = 1

def func():
	global mx_safe
	# 잠기는 높이 h 이하
	for h in range(1, mx_h + 1):
		for r in range(N):
			for c in range(N):
				if area[r][c] == h:
					sink[r][c] = 1
		safe_cnt = 0
		visited = [[0] * N for _ in range(N)]
		for r in range(N):
			for c in range(N):
				# 아직 방문하지 않았으면서 가라앉지 않은 지역에서 안전 지역 시작
				if visited[r][c] == 0 and sink[r][c] == 0:
					q.append((r, c))
					visited[r][c] = 1
					safe_cnt += 1           # 안전 지역 개수
					bfs(visited)            # 안전 지역 bfs 탐색
		mx_safe = max(safe_cnt, mx_safe)
	return mx_safe


N = int(input())
mx_h = 0
area = []
for _ in range(N):
	arr = list(map(int, input().split()))
	mx_h = max(mx_h, max(arr))      # 최대 높이 탐색
	area.append(arr)

mx_safe = 1                        # 최대 안전지역 개수 초기화 1
q = []
sink = [[0] * N for _ in range(N)]
print(func())