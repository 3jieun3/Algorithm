def Greedy():
	global S
	sorted_A = sorted(A)
	b_arr = [0] * N

	min_idx = k = 0
	while 0 in b_arr:
		for i in range(N):
			if b_arr[i] == 0:
				min_idx, k = i, i
				break
		for j in range(k + 1, N):
			if b_arr[j] == 0 and B[min_idx] > B[j]:
				min_idx = j
		b_arr[min_idx] += 1
		S += B[min_idx] * sorted_A.pop()
	return S


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0
print(Greedy())