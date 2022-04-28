import sys
input = sys.stdin.readline

def Greedy():
	global total_score
	easy, hard = 0, 0
	for i in range(N):
		if sub2[i] <= L:
			hard += 1
		elif sub1[i] <= L:
			easy += 1
	if hard >= K:
		total_score += K * 140
		return total_score
	else:
		total_score += hard * 140

	total_score += min(easy, K - hard) * 100
	return total_score


N, L, K = map(int, input().split())
sub1, sub2 = [0] * N, [0] * N
for n in range(N):
	sub1[n], sub2[n] = map(int, input().split())
total_score = 0
print(Greedy())