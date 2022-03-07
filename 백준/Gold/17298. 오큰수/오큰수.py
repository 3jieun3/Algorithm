import sys
input = sys.stdin.readline

def nge(n):
	stack = []
	top = -1
	for i in range(n-1, -1, -1):  # 거꾸로 탐색
		a_i = A_arr[i]
		while top > 0 and stack[top] <= a_i:     # 스택 top 이 a_i 보다 클때까지 pop
			stack.pop()
			top -= 1

		if top >= 0 and stack[top] > a_i:       # 스택 top 이 a_i 보다 크면 nge 저장
			nge_arr[i] = stack[top]

		stack.append(a_i)                       # 스택에 push
		top += 1


N = int(input())
A_arr = list(map(int, input().split()))
nge_arr = [-1] * N      # 모두 없다는 가정
nge(N)
print(*nge_arr)