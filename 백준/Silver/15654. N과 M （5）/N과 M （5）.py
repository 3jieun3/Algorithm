def perm(cnt, arr):     # nPm
	if cnt == M:
		print(*arr)
		return

	for i in range(N):
		if bit[i] == 0:
			bit[i] = 1
			perm(cnt + 1, arr + [numbers[i]])
			bit[i] = 0


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
bit = [0] * N
perm(0, [])