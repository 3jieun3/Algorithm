from collections import deque

def last_card(n):
	q = deque()
	for x in range(1, n + 1):
		q.append(x)
	while len(q) > 1:
		q.popleft()
		q.append(q.popleft())
	return q.popleft()


print(last_card(int(input())))