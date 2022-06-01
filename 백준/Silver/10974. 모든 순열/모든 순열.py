def permutation(cnt, perm):
	if cnt == N:
		print(*perm)
		return

	for i in range(1, N + 1):
		if bit[i] == 0:
			bit[i] = 1
			permutation(cnt + 1, perm + [i])
			bit[i] = 0


N = int(input())
bit = [0] * (N + 1)
permutation(0, [])