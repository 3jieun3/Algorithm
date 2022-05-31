def perm(i, cnt):
	if cnt == M:
		print(*arr)
		return
	if i == N + 1:
		return

	for j in range(N):
		if i == j + 1:
			continue
		if bit[j] == 0:
			arr.append(j + 1)
			bit[j] = 1
			perm(j + 1, cnt + 1)
			arr.pop()
			bit[j] = 0


N, M = map(int, input().split())
bit = [0] * N
arr = []
perm(0, 0)