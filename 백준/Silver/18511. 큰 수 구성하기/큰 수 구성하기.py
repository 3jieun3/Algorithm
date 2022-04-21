def rep_permutation(i, n, r, num):
	global max_num
	if num > N:
		return
	if i == r:
		if max_num < num:
			max_num = num
		return

	for j in range(n):
		rep_permutation(i + 1, n, r, num * 10 + K_arr[j])


N, K = map(int, input().split())
K_arr = list(map(int, input().split()))
K_arr.sort(reverse=True)
max_num = 0
for cnt in range(len(str(N)), 0, -1):
	rep_permutation(0, K, cnt, 0)
print(max_num)