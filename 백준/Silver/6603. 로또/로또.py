import sys
input = sys.stdin.readline

def lotto_combi(i, cnt, combi):
	if cnt == 6:
		results.append(combi)
		return

	for j in range(i, k):
		lotto_combi(j + 1, cnt + 1, combi + [S[j]])


results = []
while True:
	testcase = list(map(int, input().split()))
	if testcase[0] == 0:
		break
	k, S = testcase[0], testcase[1:]
	results.append([])
	lotto_combi(0, 0, [])

for results in results[1:]:
	print(*results)