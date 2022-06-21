import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    q = deque()
    q.append(n)
    
    while q:
        now = q.popleft()
        if now == k:
            break
        else:
            for nxt in (now-1, now+1, 2*now):
                if 0<=nxt<=Max and visit_time[nxt] == 0:
                    q.append(nxt)
                    visit_time[nxt] = visit_time[now]+1

Max = 10**5           
n, k = map(int, input().split())
visit_time = [0]*(Max+1)
bfs()
print(visit_time[k])