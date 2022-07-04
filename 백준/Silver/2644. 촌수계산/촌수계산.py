import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs():
	while q:
		n1 = q.pop(0)
		cnt = visited[n1]
		if n1 == man2:
			return cnt
		for n2 in range(1, n + 1):
			# 인접해있고 촌수 계산 안했던 사람
			if adj[n1][n2] == 1 and visited[n2] == -1:
				visited[n2] = cnt + 1       # 방문처리 (촌수)
				q.append(n2)
	return -1


def dfs(v, visited):
	if v == man2:           # 원하는 사람 찾은 경우 종료
		return
	for w in range(1, n + 1):
		# 인접하고 촌수 계산 아직 안되어있는 사람
		if adj[v][w] == 1 and visited[w] == -1:
			visited[w] = visited[v] + 1
			dfs(w, visited)


n = int(input())
man1, man2 = map(int, input().split())
# 부모 자식 관계
m = int(input())
adj = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
	# x는 y의 부모
	x, y = map(int, input().split())
	adj[x][y] += 1
	adj[y][x] += 1

# q = [man1]
# print(bfs())      # bfs 방법

visited = [-1] * (n + 1)
visited[man1] = 0
dfs(man1, visited)
print(visited[man2])
