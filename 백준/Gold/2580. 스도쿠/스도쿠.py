import sys
input = sys.stdin.readline

# 행 방향 num 가능성 체크
def row_check(r, num):
    for j in range(9):      # 0 ~ 해당 열까지 체크
        if sudoku[r][j] == num:
            return False
    return True

# 열 방향 num 가능성 체크
def col_check(c, num):
    for i in range(9):      # 0 ~ 해당 행까지 체크
        if sudoku[i][c] == num:
            return False
    return True

# 정사각형에서 num 가능성 체크
def square_check(r, c, num):
    # 정사각형 내의 가운데 위치
    mid_r = (r // 3) * 3 + 1
    mid_c = (c // 3) * 3 + 1
    for i in [mid_r - 1, mid_r, mid_r + 1]:
        for j in [mid_c - 1, mid_c, mid_c + 1]:
            if sudoku[i][j] == num:
                return False
    return True


def dfs(idx):
    global flag
    # 모든 빈칸 해결한 경우 종료
    if idx == len(blank_pos):
        flag = True
        for row in range(9):
            print(*sudoku[row])
        return

    r, c = blank_pos[idx]
    for num in range(1, 10):
        # num 이 행, 열, 정사각형 구역 모두 만족하면
        if row_check(r, num) and col_check(c, num) and square_check(r, c, num):
            sudoku[r][c] = num
            dfs(idx + 1)
            if flag:
                return
            sudoku[r][c] = 0


sudoku = [list(map(int, input().split())) for _ in range(9)]

# 빈칸 위치 저장
blank_pos = []
for row in range(9):
    for col in range(9):
        if sudoku[row][col] == 0:
            blank_pos.append((row, col))

flag = False
dfs(0)
