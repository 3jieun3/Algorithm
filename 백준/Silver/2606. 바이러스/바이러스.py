import sys
input = sys.stdin.readline

n = int(input())
e = int(input())
adj = {}

for i in range(1, n+1): adj[i] = []
    
for _ in range(e):
    conn = list(map(int, input().split()))
    adj[conn[0]].append(conn[1])
    adj[conn[1]].append(conn[0])

def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            nxt = [x for x in graph[now] if x not in visited]
            stack += nxt
    return visited
            
print(len(dfs(adj, 1))-1)