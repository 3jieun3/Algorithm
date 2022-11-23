from collections import deque

def move_recur(cur, nxt):
    # 100 이내 번호이면 이동
    if nxt <= 100:
        cur = nxt
    # 사다리 및 뱀 있는 경우 이동
    if ladder_snake_info[cur]:
        cur = move_recur(cur, ladder_snake_info[cur])
    return cur

def bfs():
    while que:
        cur = que.popleft()
        if cur == 100:  # bfs 종료 조건
            return board[cur]
        dice_cnt = board[cur]
        for d in range(1, 7):    # 주사위 굴려 칸 이동
            nxt = move_recur(cur, cur + d)
            # 해당 칸에 도착하기위한 최소 주사위 횟수 저장
            if board[nxt] == 0 or board[nxt] > dice_cnt + 1:
                board[nxt] = dice_cnt + 1
                que.append(nxt)

N, M = map(int, input().split())    # N: 사다리 수, M: 뱀 수
# 사다리 & 뱀 정보 1차원 배열 저장
ladder_snake_info = [0 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())    # x번 -> y번 (x < y) (1, 100제외)
    ladder_snake_info[x] = y
for _ in range(M):
    u, v = map(int, input().split())    # u번 -> v번 (u > v) (1, 100제외)
    ladder_snake_info[u] = v

board = [0 for _ in range(101)]     # 보드판 1차원 배열 (index = 칸 번호)
que = deque([1])
print(bfs())