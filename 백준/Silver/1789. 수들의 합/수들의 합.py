memo = [0] * 100001
for x in range(1, 100001):
	memo[x] = memo[x - 1] + x

S = int(input())
n = 1                                   # 서로 다른 자연수 개수
for x in range(1, S):
	if S - memo[x] >= (x + 1):          # 다음 자연수 아직 더해도 되는 경우
		n += 1
	elif S - memo[x] < (x + 1):         # 다음 자연수 더하면 S 초과하는 경우
		break
print(n)