import sys
input = sys.stdin.readline

def bfs():
	q.append(0)
	visited[0] = 1
	while q:
		now = q.pop(0)

		if now == (n + 1):      # 페스티벌 도착
			return "happy"

		for nxt in range(n + 2):
			if nxt == now:
				continue
			# 1000 미터 거리 이내에 있고 방문하지 않았던 위치
			if distance[now][nxt] <= 1000 and visited[nxt] == 0:
				q.append(nxt)
				visited[nxt] = visited[now] + 1

	return "sad"                # 불가능


def dist():
	for i in range(n + 2):
		x1, y1 = pos[i]
		for j in range(i + 1, n + 2):
			x2, y2 = pos[j]
			distance[i][j] = abs(x1 - x2) + abs(y1 - y2)
			distance[j][i] = abs(x1 - x2) + abs(y1 - y2)


T = int(input())
results = []
for tc in range(T):
	n = int(input())
	# 상근 집 (0) - 편의점s (1 ~ n) - 페스티벌(n+1)
	pos = [list(map(int, input().split())) for _ in range(n + 2)]
	visited = [0] * (n + 2)

	# 각 위치간의 거리
	distance = [[0] * (n + 2) for _ in range(n + 2)]
	dist()

	q = []
	results.append(bfs())

print(*results, sep="\n")