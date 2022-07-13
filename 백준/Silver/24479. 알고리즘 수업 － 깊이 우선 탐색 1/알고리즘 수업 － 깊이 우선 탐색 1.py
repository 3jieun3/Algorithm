import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n):
	global o
	order[n] = o
	o += 1
	for m in adj[n]:
		if order[m] == 0:
			dfs(m)


# 정점수, 간선수, 시작정점
N, M, R = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
	u, v = map(int, input().split())
	adj[u].append(v)
	adj[v].append(u)

# 노드 오름차순 정렬
for i in range(1, N + 1):
	adj[i].sort()


order = [0] * (N + 1)
o = 1

dfs(R)
print(*order[1:], sep="\n")