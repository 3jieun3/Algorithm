import sys
input = sys.stdin.readline

dr = [-1, -2, -2, -1, 1, 2,  2,  1]
dc = [-2, -1,  1,  2, 2, 1, -1, -2]

def bfs():
	q.append(start)
	board[start[0]][start[1]] = 1
	while q:
		r, c = q.pop(0)
		cnt = board[r][c]
		if (r, c) == end:
			return cnt - 1                      # 시작점 제외
		for k in range(8):
			nr = r + dr[k]
			nc = c + dc[k]
			if 0 > nr or nr >= l or 0 > nc or nc >= l:
				continue
			if board[nr][nc] == 0:
				q.append((nr, nc))
				board[nr][nc] = cnt + 1         # 방문 처리(순번)


T = int(input())
results = [0] * T
for tc in range(T):
	l = int(input())
	start = tuple(map(int, input().split()))
	end = tuple(map(int, input().split()))
	board = [[0] * l for _ in range(l)]
	q = []
	results[tc] = bfs()
	
print(*results, sep="\n")