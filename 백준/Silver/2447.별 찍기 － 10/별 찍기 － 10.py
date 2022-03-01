import sys
input = sys.stdin.readline

def star_recur(n, start_r, start_c):
	m = n // 3
	# n >= 3 인 경우 (n/3)×(n/3) 9분할 & (i, j) = 각 분할의 (0,0)자리 인덱스
	for i in range(start_r, start_r + n, m):
		for j in range(start_c, start_c + n, m):
			# n x n 의 가운데 분할인 경우
			if (i, j) == (start_r + m, start_c + m):
				continue
			else:
				if n == 3:  # 기준이 되는 3x3 인 경우 (m = 1 이므로 위의 반복문으로 한자리씩 9분할됨)
					pattern[i][j] = '*'
				else:       # 그 외의 경우 재귀로 분할
					star_recur(m, i, j)


N = int(input())
pattern = [[' '] * N for _ in range(N)]  # 공백으로 초기화

star_recur(N, 0, 0)

for pt in pattern:
	print(*pt, sep='')