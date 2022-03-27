def permutation(i, n, m):               # (1) n개 중에서 중복 없이 m개를 고른 순열 = nPm
	# 가지치기
	if i == m:
		save_perm_elements(numbers[:i], perm)
		return
	# 기본 파트
	if i == n:
		return
	# 유도파트
	for j in range(i, n):
		numbers[i], numbers[j] = numbers[j], numbers[i]
		permutation(i + 1, n, m)
		numbers[i], numbers[j] = numbers[j], numbers[i]

def combination(i, n, cnt, m):          # (2) n개 중에서 중복 없이 m개를 고른 조합 = nCm
	# 가지치기
	if cnt == m:
		save_combi_elements(bit, combi)
		return
	# 기본 파트
	if i == n:
		return
	# 유도 파트
	bit[i] = 1
	combination(i + 1, n, cnt + 1, m)
	bit[i] = 0
	combination(i + 1, n, cnt, m)

def permutation_rep(i, n, m):           # (3) n개 중에서 중복 있게 m개 고른 순열 = nㅠm
	# 가지치기
	if i == m:
		save_perm_elements(nums, perm_rep)
		return
	# 기본파트
	if i == n:
		return
	# 유도 파트
	for j in range(n):
		nums[i] = numbers[j]
		permutation_rep(i + 1, n, m)

def combination_rep(i, n, cnt, m):      # (4) n개 중에서 중복 있게 m개 고른 조합 = nHm ?
	# 가지치기
	if cnt == m:
		save_combi_rep_elements(cnt_rep, combi_rep)
		return
	# 기본파트
	if cnt == n:
		return
	# 유도파트
	for j in range(i, n):
		cnt_rep[j] += 1
		combination_rep(i, n, cnt + 1, m)
		cnt_rep[j] -= 1

def save_perm_elements(mid_arr, rst_arr):
	temp = []
	for i in range(len(mid_arr)):
		temp.append(mid_arr[i])
	rst_arr.append(temp)

def save_combi_elements(mid_arr, rst_arr):
	temp = []
	for i in range(len(mid_arr)):
		if mid_arr[i]:
			temp.append(numbers[i])
	rst_arr.append(temp)

def save_combi_rep_elements(mid_arr, rst_arr):
	temp = []
	for i in range(len(mid_arr)):
		for _ in range(mid_arr[i]):
			temp.append(numbers[i])
	if temp not in rst_arr:
		rst_arr.append(temp)

def print_result(arr):
	arr.sort(key=lambda x: tuple(x[i] for i in range(len(x))))
	for rst in arr:
		print(*rst)


N, M = map(int, input().split())
numbers = [x for x in range(1, N + 1)]

nums = [0] * M
perm_rep = []
permutation_rep(0, N, M)
print_result(perm_rep)