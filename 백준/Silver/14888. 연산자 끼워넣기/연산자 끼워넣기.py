import sys
input = sys.stdin.readline

def recur(i, rst, add, sub, mul, div):
	global mn, mx
	if i == N:
		if mn > rst:
			mn = rst
		if mx < rst:
			mx = rst
		return

	if add:
		recur(i + 1, rst + A[i], add - 1, sub, mul, div)
	if sub:
		recur(i + 1, rst - A[i], add, sub - 1, mul, div)
	if mul:
		recur(i + 1, rst * A[i], add, sub, mul - 1, div)
	if div:
		recur(i + 1, int(rst / A[i]), add, sub, mul, div - 1)



N = int(input())
A = list(map(int, input().split()))
numbers = list(map(int, input().split()))   # +, -, *, %
mn, mx = 1000000000, -1000000000
recur(1, A[0], *numbers)
print(mx)
print(mn)