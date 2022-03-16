import sys
input = sys.stdin.readline

def chess_coloring(r_idx, c_idx):
	cnt_W, cnt_B = 0, 0
	for r in range(r_idx, r_idx + 8):
		for c in range(c_idx, c_idx + 8):
			# WB 시작 - 홀수 행 = 홀수 열 - B, 짝수 열 - W
			# BW 시작 - 홀수 행 = 홀수 열 - W, 짝수 열 - B
			if r % 2 and c % 2:
				if board[r][c] == 'W':
					cnt_W += 1
				else:
					cnt_B += 1
			elif r % 2 and not c % 2:
				if board[r][c] == 'B':
					cnt_W += 1
				else:
					cnt_B += 1

			# WB 시작 - 짝수 행 = 홀수 열 - W, 짝수 열 - B
			# BW 시작 - 짝수 행 = 홀수 열 - B, 짝수 열 - W
			elif not r % 2 and c % 2:
				if board[r][c] == 'B':
					cnt_W += 1
				else:
					cnt_B += 1
			else:
				if board[r][c] == 'W':
					cnt_W += 1
				else:
					cnt_B += 1

	if cnt_W < cnt_B:
		return cnt_W
	return cnt_B


def divide_bruteforce():
	rst = M * N
	for i in range(N - 8 + 1):
		for j in range(M - 8 + 1):
			tmp = chess_coloring(i, j)
			if tmp < rst:
				rst = tmp
	return rst


N, M = map(int, input().split())    # N 행 M 열
board = []
for _ in range(N):
    board.append(list(input()))
print(divide_bruteforce())