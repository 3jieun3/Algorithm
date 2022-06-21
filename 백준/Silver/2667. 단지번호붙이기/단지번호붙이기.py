import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
	num = 0
	sizes = []
	for i in range(N):
		for j in range(N):
			if arr[i][j] and visited[i][j] == 0:
				num += 1                # 단지 번호
				size = 1                # 단지 내 가구 수
				visited[i][j] = num
				q.append((i, j))
				while q:
					r, c = q.pop(0)
					num = visited[r][c]
					for k in range(4):
						nr = r + dr[k]
						nc = c + dc[k]
						if 0 > nr or nr >= N or 0 > nc or nc >= N:
							continue
						if arr[nr][nc] and visited[nr][nc] == 0:
							size += 1
							visited[nr][nc] = num
							q.append((nr, nc))
				sizes.append(size)
	print(num)
	print(*sorted(sizes), sep='\n')


N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
q = []
bfs()