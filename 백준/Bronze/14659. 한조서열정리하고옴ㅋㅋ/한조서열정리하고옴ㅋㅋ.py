def Greedy():
	max_cnt = 0
	for i in range(N - 1):
		now = heights[i]
		cnt = 0
		if max_cnt > N - i:
			return max_cnt
		for j in range(i + 1, N):
			if now > heights[j]:
				cnt += 1
			else:
				break
		if max_cnt < cnt:
			max_cnt = cnt
	return max_cnt


N = int(input())
heights = list(map(int, input().split()))
print(Greedy())