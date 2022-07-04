import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs():
	while q:
		n = q.pop(0)
		for m in adj[n]:
			# n과 인접하면서 parent가 아직 정해지지 않은 노드
			if parent[m] == 0:
				parent[m] = n
				q.append(m)

def dfs(n):
	for m in adj[n]:            # n 에 인접하면서 parent 아직 정해지지 않은 노드
		if parent[m] == 0:
			parent[m] = n
			dfs(m)


N = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
	n1, n2 = map(int, input().split())
	adj[n1] += [n2]
	adj[n2] += [n1]

parent = [0] * (N + 1)      # 부모 노드

# q = [1]
# bfs()                       # bfs 방법

dfs(1)                         # 루트노드(1) 에서 dfs

print(*parent[2:], sep="\n")