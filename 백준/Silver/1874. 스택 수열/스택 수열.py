def stack_operation(n):
	stack = []
	result = []
	target_idx = 0                      # 수열에서 완성해야할 정수의 인덱스
	for m in range(1, n + 1):           # 1 ~ n 정수 push
		stack.append(m)
		operation.append('+')

        # stack top 이 타겟 정수가 아닐때까지 pop
		while len(stack) > 0 and stack[-1] == series[target_idx]:
			result.append(stack.pop())
			operation.append('-')
			if target_idx == (n - 1):   # 수열 모두 완성한 경우
				return True
			else:                       # 아닌 경우 타겟인덱스 + 1
				target_idx += 1
	return False


series = []
operation = []
N = int(input())
for i in range(N):
	series.append(int(input()))
if stack_operation(N):
	print(*operation, sep='\n')
else:
	print('NO')