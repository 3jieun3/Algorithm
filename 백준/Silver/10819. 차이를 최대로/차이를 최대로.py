import sys
input = sys.stdin.readline

def func(i, cur_diff):
	global max_diff

	if i == N:
		if cur_diff > max_diff:
			max_diff = cur_diff
		return

	for j in range(i, N):
		A[i], A[j] = A[j], A[i]
		if i == 0:
			func(i + 1, cur_diff)
		else:
			func(i + 1, cur_diff + abs(A[i - 1] - A[i]))
		A[i], A[j] = A[j], A[i]


N = int(input())
A = list(map(int, input().split()))
max_diff = 0
func(0, 0)
print(max_diff)