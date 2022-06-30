import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(visited):
	while q:
		r, c = q.pop(0)
		for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			nr = r + dr
			nc = c + dc
			if 0 > nr or nr >= N or 0 > nc or nc >= N:
				continue
			# 가라앉지 않은 지역 탐색
			if visited[nr][nc] == 0 and sink[nr][nc] == 0:
				q.append((nr, nc))
				visited[nr][nc] = 1

def dfs(r, c, visited):
	# 방문 처리
	visited[r][c] = 1
	# 델타 검색
	for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
		nr = r + dr
		nc = c + dc
		if 0 > nr or nr >= N or 0 > nc or nc >= N:
			continue
		# 가라앉지 않은 지역 탐색
		if visited[nr][nc] == 0 and sink[nr][nc] == 0:
			dfs(nr, nc, visited)

def func():
	global mx_safe
	# 잠기는 높이 h 이하에서
	for h in range(1, mx_h + 1):
		for r in range(N):
			for c in range(N):
				if area[r][c] == h:
					sink[r][c] = 1      # 잠기는 지역 표시

		safe_cnt = 0
		visited = [[0] * N for _ in range(N)]
		for r in range(N):
			for c in range(N):
				# 아직 방문하지 않았으면서 가라앉지 않은 지역에서 안전 지역 시작
				if visited[r][c] == 0 and sink[r][c] == 0:
					q.append((r, c))
					visited[r][c] = 1
					safe_cnt += 1           # h높이 물에서 안전 지역 개수
					# bfs(visited)            # 안전 지역 bfs 탐색
					dfs(r, c, visited)          # 안전 지역 dfs 탐색
		mx_safe = max(safe_cnt, mx_safe)
	return mx_safe


N = int(input())
mx_h = 0
area = []
for _ in range(N):
	arr = list(map(int, input().split()))
	mx_h = max(mx_h, max(arr))      # 최대 높이 탐색
	area.append(arr)

mx_safe = 1
q = []
sink = [[0] * N for _ in range(N)]
print(func())