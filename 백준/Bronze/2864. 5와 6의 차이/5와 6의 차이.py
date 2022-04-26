# 최소 : 모두 5 , 최대 : 모두 6
def Greedy(a, b):
	mn, mx = a + b, a + b       # 원래 합으로 초기화
	for num in [a, b]:
		diff = 1                # 특정 자릿수에서 5일때와 6일때의 차이 (일의 자리일때로 초기화)
		while num:
			if num % 10 == 5:       # 5 인 경우 -> 6 인 경우가 최대
				mx += diff          # 차이만큼 더함
			elif num % 10 == 6:     # 6 인 경우 -> 5 인 경우가 최소
				mn -= diff          # 차이만큼 뻄
			diff *= 10
			num //= 10
	return mn, mx


A, B = map(int, input().split())
print(*Greedy(A, B))