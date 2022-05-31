import sys
input = sys.stdin.readline

def func():
	# 다르면 1 같으면 0
	one_cnt = 0
	for i in range(N):
		for j in range(M):
			if A[i][j] != B[i][j]:
				mtx[i][j] += 1
				one_cnt += 1
	# A = B 인 경우
	if one_cnt == 0:
		return 0
	# 3 * 3 보다 작은 경우
	if N < 3 or M < 3:
		return -1
	cnt = 0
	for i in range(N):
		for j in range(M):
			# 다른 위치에서 토글
			if mtx[i][j] == 1:
				# 해당 위치부터 3 * 3 행렬 바꿀 수 없음
				if N - 2 <= i < N or M - 2 <= j < M:
					return -1
				for ni in range(i, i + 3):
					for nj in range(j, j + 3):
						mtx[ni][nj] = (mtx[ni][nj] + 1) % 2
				cnt += 1
	return cnt


N, M = map(int, input().split())
A = [list(map(int, list(input().rstrip()))) for _ in range(N)]
B = [list(map(int, list(input().rstrip()))) for _ in range(N)]
mtx = [[0] * M for _ in range(N)]
print(func())