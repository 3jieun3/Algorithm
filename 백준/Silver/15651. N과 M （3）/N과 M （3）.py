def rep_perm(cnt, perm):    # nㅠr
	if cnt == M:
		print(*perm)
		return

	for i in range(N):
		rep_perm(cnt + 1, perm + [i + 1])


N, M = map(int, input().split())
rep_perm(0, [])