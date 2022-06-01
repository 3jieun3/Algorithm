def rep_combi(i, cnt, combi):  # nHr
	if cnt == M:
		print(*combi)
		return

	for j in range(i, N):
		rep_combi(j, cnt + 1, combi + [j + 1])


N, M = map(int, input().split())
rep_combi(0, 0, [])