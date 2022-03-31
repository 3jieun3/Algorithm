def diagonal_check(r, c):
	for i in range(N):
		if i > 0 and 0 <= r - i < N and 0 <= c - i < N:   # 2사분면 방향 대각선에 다른 퀸 존재하는 경우
			if board[r - i][c - i] == 1:
				return False
		if i > 0 and 0 <= r - i < N and 0 <= c + i < N:   # 1사분면 방향 대각선에 다른 퀸 존재하는 경우
			if board[r - i][c + i] == 1:
				return False
	return True

def DFS_backtracking(r, c):
	global case_cnt
	if not diagonal_check(r, c):            # 가지치기 - 대각선에서 중복 배치 불가능
		return

	if r + 1 == N:                          # 기본 파트 - 모든 행 탐색 완료시 종료
		case_cnt += 1
		return

	for nc in range(N):                     # 유도 파트 - r + 1 행의 모든 열 탐색
		if col_flag[nc]:                    # 해당 열에 이미 있으면 진행하지 않음
			continue
		if nc == c + 1 or nc == c - 1:      # (r, c)의 대각선열이면 진행하지 않음
			continue
		board[r + 1][nc] += 1
		col_flag[nc] = True
		DFS_backtracking(r + 1, nc)
		board[r + 1][nc] = 0
		col_flag[nc] = False

def N_queen():
	for j in range(N):                  # 0 행 모든 열을 순차적으로 루트로
		board[0][j] += 1
		col_flag[j] = True
		DFS_backtracking(0, j)
		board[0][j] -= 1
		col_flag[j] = False
	return case_cnt


N = int(input())
board = [[0] * N for _ in range(N)]
col_flag = [False] * N
case_cnt = 0
print(N_queen())