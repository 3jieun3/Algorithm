import sys
from collections import deque
input = sys.stdin.readline

def bfs(week_flag):
    # 적록색약이 아닌 경우
    if not week_flag:
        while q:
            r, c = q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if 0 > nr or nr >= N or 0 > nc or nc >= N:
                    continue
                if paint[nr][nc] == paint[r][c] and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
    # 적록색약인 경우
    else:
        while q:
            r, c = q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if 0 > nr or nr >= N or 0 > nc or nc >= N:
                    continue
                if paint[nr][nc] == paint[r][c] and visited[nr][nc] == 1:
                    visited[nr][nc] = 2
                    q.append((nr, nc))
                elif (paint[r][c] in ['R', 'G'] and paint[nr][nc] in ['R', 'G']) and visited[nr][nc] == 1:
                    visited[nr][nc] = 2
                    q.append((nr, nc))


N = int(input())
paint = [input() for _ in range(N)]

q = deque()
visited = [[0] * N for _ in range(N)]
no_area, yes_area = 0, 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            visited[i][j] = 1
            q.append((i, j))
            no_area += 1
            bfs(False)

for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            visited[i][j] = 2
            q.append((i, j))
            yes_area += 1
            bfs(True)

print(no_area, yes_area)