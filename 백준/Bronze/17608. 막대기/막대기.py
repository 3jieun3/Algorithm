import sys
input = sys.stdin.readline

def visible_sticks(n):
	stack = [heights.pop()]                     # 오른쪽부터 pop 하여
	while heights:
		h = heights.pop()
		if len(stack) > 0 and stack[-1] < h:    # stack top 의 높이보다 클때만
			stack.append(h)                     # append
	return len(stack)


N = int(input())
heights = []
for _ in range(N):
	heights.append(int(input()))
print(visible_sticks(N))