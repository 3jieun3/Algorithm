import sys
input = sys.stdin.readline

def dfs(r, c, move, path):
    global max_move

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if 0 > nr or nr >= R or 0 > nc or nc >= C:
            continue
        if alpha[ord(board[nr][nc]) - ord("A")] == 0:
            alpha[ord(board[nr][nc]) - ord("A")] = 1
            dfs(nr, nc, move + 1, path + board[r][c])
            alpha[ord(board[nr][nc]) - ord("A")] = 0

    if move > max_move:
        max_move = move


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

max_move = 0

alpha = [0] * 26
alpha[ord(board[0][0]) - ord("A")] = 1

dfs(0, 0, 1, board[0][0])

print(max_move)