def pipe_cutting(n):
	cnt = 0
	pipe = 0
	stack = []
	for i in range(n):
		bracket = laser[i]
		if bracket == ')':
			if len(stack) > 0 and stack[-1] == '(':     # 레이저 표시 의미
				pipe -= 1                               # top 의 '(' 에 추가한 막대기 하나 취소
				cnt += pipe                             # 현재까지의 막대기 개수대로 조각 생김
			elif len(stack) > 0 and stack[-1] == ')':   # 막대기 하나의 끝 의미
				pipe -= 1                               # 막대기 하나 감소
				cnt += 1                                # 끝날때 조각 하나 생기므로 조각 수 증가
		else:   # bracket == '('
			pipe += 1                                   # '(' 는 막대기의 시작으로 가정하고 막대기 수 추가
			
		stack.append(bracket)
	return cnt


laser = list(input())
print(pipe_cutting(len(laser)))