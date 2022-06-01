import sys
input = sys.stdin.readline

def TSP_backtracking(cur_w, perm):
	global min_weight

	if cur_w >= min_weight:
		return

	if len(perm) == N:
		# 시작 도시로 다시 갈 수 없는 경우 제외
		if W[perm[-1]][perm[0]] == 0:
			return
		# 시작 도시로 가는 비용 합
		cur_w += W[perm[-1]][perm[0]]
		if min_weight > cur_w:
			min_weight = cur_w
		return

	for i in range(1, N + 1):
		# 방문 도시 제외
		if visited[i] == 1:
			continue
		# 갈 수 없는 도시 제외
		if perm and W[perm[-1]][i] == 0:
			continue
		w = 0
		if perm:
			w = W[perm[-1]][i]
		visited[i] = 1
		TSP_backtracking(cur_w + w, perm + [i])
		visited[i] = 0


N = int(input())
W = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
min_weight = 9999999999
visited = [0] * (N + 1)
TSP_backtracking(0, [])
print(min_weight)