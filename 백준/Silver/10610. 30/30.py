def Greedy():
	arr = list(map(int, list(N)))
	if 0 not in arr:    # 10 의 배수가 될 수 없으면 제외
		return -1
	if sum(arr) % 3:    # 3의 배수가 될 수 없으면 제외
		return -1

	ans = 0
	arr.sort(reverse=True)
	for i in range(len(arr)):
		ans = ans * 10 + arr[i]
	return ans


N = input()
print(Greedy())