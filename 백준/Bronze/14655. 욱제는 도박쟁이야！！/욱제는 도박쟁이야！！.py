def Greedy():
	# 1라운드: 모두 양수일때 최대
	ans = sum(map(abs, rounds[0]))
	# 2라운드: 모두 음수일때 최소
	ans += sum(map(lambda x: (x if x >= 0 else -x), rounds[1]))
	return ans


N = int(input())
rounds = [list(map(int, input().split())) for _ in range(2)]
print(Greedy())