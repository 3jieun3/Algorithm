import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(r, c, move, num):
	if move == 5:               # 다섯번 이동 완료한 경우
		n = ''.join(num)
		if n not in numbers:
			numbers.append(n)
		return

	for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
		nr, nc = r + dr, c + dc
		if 0 > nr or nr >= 5 or 0 > nc or nc >= 5:
			continue
		dfs(nr, nc, move + 1, num + [board[nr][nc]])


board = [list(input().split()) for _ in range(5)]
numbers = []
# 모든 위치에서 시작하여 dfs
for i in range(5):
	for j in range(5):
		dfs(i, j, 0, [board[i][j]])
print(len(numbers))