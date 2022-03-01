import sys
input = sys.stdin.readline

def fibo_recur(n):
	if n <= 1:
		return n
	return fibo_recur(n-1) + fibo_recur(n-2)


N = int(input())
print(fibo_recur(N))