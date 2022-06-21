import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
	num = 0
	for i in range(N):
		for j in range(M):
			if arr[i][j] and visited[i][j] == 0:
				num += 1                # 지렁이 수
				visited[i][j] = num
				q.append((i, j))
				while q:
					r, c = q.pop(0)
					for k in range(4):
						nr = r + dr[k]
						nc = c + dc[k]
						if 0 > nr or nr >= N or 0 > nc or nc >= M:
							continue
						if arr[nr][nc] and visited[nr][nc] == 0:
							visited[nr][nc] = num
							q.append((nr, nc))
	return num


T = int(input())
results = []
for tc in range(T):
	M, N, K = map(int, input().split())
	arr = [[0] * M for _ in range(N)]
	visited = [[0] * M for _ in range(N)]
	for _ in range(K):
		X, Y = map(int, input().split())
		arr[Y][X] += 1
	q = []
	results.append(bfs())
print(*results, sep='\n')