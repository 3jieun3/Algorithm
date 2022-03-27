# 가지치기 어떻게?
import sys
input = sys.stdin.readline

def calcul_dfs(i, n, rst):
	global min_rst, max_rst
	if i == n:
		if rst > max_rst:
			max_rst = rst
		if rst < min_rst:
			min_rst = rst
		return

	for j in range(i, n):
		op_arr[i], op_arr[j] = op_arr[j], op_arr[i]
		if op_arr[i] == 0:
			calcul_dfs(i + 1, n, rst + Array[i])
		elif op_arr[i] == 1:
			calcul_dfs(i + 1, n, rst - Array[i])
		elif op_arr[i] == 2:
			calcul_dfs(i + 1, n, rst * Array[i])
		else:
			calcul_dfs(i + 1, n, int(rst / Array[i]))
		op_arr[i], op_arr[j] = op_arr[j], op_arr[i]


N = int(input())                            # 수 개수 2 ≤ N ≤ 11
Array = list(map(int, input().split()))     # 1 ≤ 수열 ≤ 100
int_arr = list(map(int, input().split()))   # +, -, x, % 개수

op_arr = [0]                                # 연산자 배열 ([1] ~ [N - 1])
for o in range(4):
	for _ in range(int_arr[o]):
		op_arr.append(o)

min_rst, max_rst = 10**9, -10**9             # 최솟값, 최댓값
calcul_dfs(1, N, Array[0])
print(max_rst)
print(min_rst)
