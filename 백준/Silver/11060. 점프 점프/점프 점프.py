import sys
input = sys.stdin.readline

def bfs():
	while q:
		i = q.pop(0)
		if i == N - 1:
			return visited[-1]
		for dj in range(1, A[i] + 1):
			j = i + dj
			if j >= N:
				continue
			if visited[j] > visited[i] + 1:
				visited[j] = visited[i] + 1
				q.append(j)
	return -1


N = int(input())
A = list(map(int, input().split()))

min_jump = 999999999
q = [0]
visited = [min_jump] * N
visited[0] = 0
print(bfs())