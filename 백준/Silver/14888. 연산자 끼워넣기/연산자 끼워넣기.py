# DFS
import sys
input = sys.stdin.readline

def calcul_dfs(i, n, rst, op):
	global min_rst, max_rst
	if i == n:
		if rst > max_rst:
			max_rst = rst
		if rst < min_rst:
			min_rst = rst
		return

	if op[0]:
		op[0] -= 1
		calcul_dfs(i + 1, n, rst + A[i], op)
		op[0] += 1
	if op[1]:
		op[1] -= 1
		calcul_dfs(i + 1, n, rst - A[i], op)
		op[1] += 1
	if op[2]:
		op[2] -= 1
		calcul_dfs(i + 1, n, rst * A[i], op)
		op[2] += 1
	if op[3]:
		op[3] -= 1
		calcul_dfs(i + 1, n, int(rst / A[i]), op)
		op[3] += 1


N = int(input())                            # 수 개수 2 ≤ N ≤ 11
A = list(map(int, input().split()))         # 1 ≤ 수열 ≤ 100
op_arr = list(map(int, input().split()))    # +, -, x, % 개수

min_rst, max_rst = 10**9, -10**9              # 최솟값, 최댓값
calcul_dfs(1, N, A[0], op_arr)
print(max_rst)
print(min_rst)
