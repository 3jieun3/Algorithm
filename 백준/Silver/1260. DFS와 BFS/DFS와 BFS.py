import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, start):
    visited = []
    stack = [start]
    
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            nxt = [v for v in graph[now][::-1] if v not in visited]
            stack = stack + nxt
    return visited

def bfs(graph, start):
    visited = [start]
    q = deque([start])
    
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if nxt not in visited:
                q.append(nxt)
                visited.append(nxt)
    return visited


n, m, v = map(int, input().split())
# 인접 리스트 초기화
adj = {}
for i in range(1, n+1): adj[i] = []
# 인접 리스트 저장
for _ in range(m):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
    
# 노드 오름차순 정렬
for vlst in adj.values(): vlst.sort()

for k in dfs(adj, v):
    print(k, end=' ')
print()
for k in bfs(adj, v):
    print(k, end=' ')