import sys
input = sys.stdin.readline

def knapsack_DP():
	for i in range(1, N + 1):
		vi, ci = things[i]          # 부피, 가치
		for j in range(1, K + 1):
			# 가방 부피 j 가 vi 보다 작으면 vi 아예 넣을 수 없음
			if j < vi:
				dp[i][j] = dp[i - 1][j]
			# 가방 부피 j 가 vi 보다 클 경우
			else:
				# i-1 물건 여부 확실한 결과 + i물건 있는 경우 & 없는 경우 중에서 큰 가치
				dp[i][j] = max(dp[i - 1][j - vi] + ci, dp[i - 1][j] + 0)
	return dp[N][K]


N, K = map(int, input().split())        # 물건 개수, 가방 부피
things = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]
print(knapsack_DP())