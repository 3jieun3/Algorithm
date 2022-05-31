import sys
input = sys.stdin.readline

def cal_nCr():
	a, b, n = 1, 1, N
	while n > N // 2:
		a *= n
		b *= (N + 1 - n)
		n -= 1
	return a // b

def cal_stats(start, link):                     # 능력치 합산 -> 차이 갱신
	global min_diff
	start_stat = 0
	link_stat = 0
	for i in range(N // 2):
		for j in range(i + 1, N // 2):
			start_stat += S[start[i]][start[j]] + S[start[j]][start[i]]
			link_stat += S[link[i]][link[j]] + S[link[j]][link[i]]

	if min_diff > abs(start_stat - link_stat):      # 최소 차이 갱신
		min_diff = abs(start_stat - link_stat)


def combi(i, r, start, link):
	global case_cnt

	if case_cnt > combi_cnt // 2:                   # 가지치기 : nCr 의 절반 계산한 경우 종료
		return
	if r == N // 2:                                 # basis part
		if len(link) < N // 2:                      # 덜 구한 link 구하기
			for k in range(start[-1] + 1, N + 1):
				link.append(k)
		case_cnt += 1
		cal_stats(start, link)
		return

	tmp = []
	for j in range(i, N + 1):                       # inductive part
		combi(j + 1, r + 1, start + [j], link + tmp)
		tmp.append(j)   # start에 포함했던 숫자 누적하여 link로


N = int(input())
S = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

combi_cnt = cal_nCr()   # nCr 경우의 수
case_cnt = 0            # combi 함수로 m개 조합 구한 수
min_diff = 999999999

combi(1, 0, [], [])
print(min_diff)