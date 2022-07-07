import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(r, c):
	global v_cnt, o_cnt
	visited[r][c] = 1               # 방문처리
	if ground[r][c] == 'v':         # 늑대수 카운트
		v_cnt += 1
	elif ground[r][c] == 'o':       # 양수 카운트
		o_cnt += 1

	for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
		nr = r + dr
		nc = c + dc
		if 0 > nr or nr >= R or 0 > nc or nc >= C:
			continue
		if ground[nr][nc] == '#':       # 울타리만나면 제외
			continue
		if visited[nr][nc] == 0:        # 방문 안했던 곳
			dfs(nr, nc)


R, C = map(int, input().split())
ground = [input().rstrip() for _ in range(R)]

rst_v, rst_o = 0, 0             # 최종 늑대수, 양수
visited = [[0] * C for _ in range(R)]
for i in range(R):
	for j in range(C):
		if visited[i][j] == 0 and ground[i][j] != '#':
			v_cnt, o_cnt = 0, 0     # 각 울타리 구역 안의 늑대수, 양수 초기화
			dfs(i, j)
			if v_cnt == 0 and o_cnt == 0:       # 둘다 없는 경우 제외
				continue
			if v_cnt < o_cnt:                   # 양이 늑대보다 많은 경우
				rst_o += o_cnt
			else:                               # 늑대가 양과 같거나 많은 경우
				rst_v += v_cnt
print(rst_o, rst_v)