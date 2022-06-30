import sys
input = sys.stdin.readline
# from collections import defaultdict
def dfs(startv):
    stack = [startv]
    visited = []
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            nxt = [v for v in adj[now][::-1] if v not in visited]
            stack = stack + nxt
    return visited

n, m = map(int, input().split())
adj = {i:[] for i in range(1, n+1)} #= adj = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n+1):
    adj[i].sort()

cnt = 0   
while adj:
    cnt += 1
    key = list(adj.keys())
    did = dfs(key[0])
    for v in did:
        adj.pop(v)
        
print(cnt)