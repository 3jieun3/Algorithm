import sys
input = sys.stdin.readline

def ability_diff(start, link):                  # 능력치 합산 -> 차이 갱신
	global min_diff
	s_start, s_link = 0, 0
	for i in range(r):
		for j in range(i + 1, r):
			s_start += S[start[i]][start[j]] + S[start[j]][start[i]]
			s_link += S[link[i]][link[j]] + S[link[j]][link[i]]

	min_diff = min(min_diff, abs(s_start - s_link))        # 최소 차이 갱신


def combination(i, cnt, combi):

	if cnt == r:                                # basis part
		toggle = [x for x in range(1, n) if x not in combi]
		ability_diff(combi, toggle)         # 능력치 계산
		return

	for j in range(i, n):                       # inductive part
		if j not in combi:                      # 이미 넣었던 i까지는 다시 넣지 않음
			combination(j + 1, cnt + 1, combi + [j])


N = int(input())
S = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

n, r = N + 1, N // 2
min_diff = 100 * 100
used_combi = []
combination(1, 0, [])
print(min_diff)