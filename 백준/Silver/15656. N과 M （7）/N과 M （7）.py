def rep_perm(cnt, arr):
	if cnt == M:
		perms.append(arr)
		return

	for i in range(N):
		rep_perm(cnt + 1, arr + [numbers[i]])


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
perms = []
rep_perm(0, [])

for p in perms:
	print(*p)