def diagonal_check(r, c):
    for dr, dc in [(-1, -1), (-1, 1)]:
        d = 0
        while True:
            d += 1
            nr = r + dr * d
            nc = c + dc * d
            if 0 > nr or nr >= N or 0 > nc or nc >= N:
                break
            if row_flag[nr] == nc:
                return True
    return False


def dfs_back(r):
    global tot_case

    if r == N:
        tot_case += 1
        return

    for c in range(N):
        # 같은 열에 퀸 있는지 체크
        if col_flag[c]:
            continue
        # 대각선 상에 퀸 있는지 체크
        if diagonal_check(r, c):
            continue

        # 가능한 경우
        row_flag[r] = c         # 해당 행에 열 위치 저장
        col_flag[c] = True      # 해당 열 사용 체크
        dfs_back(r + 1)
        row_flag[r] = 0
        col_flag[c] = False


def n_queen():
    # 0 행 모든 열 한 번씩 시작
    for c in range(N):
        row_flag[0] = c
        col_flag[c] = True
        dfs_back(1)
        col_flag[c] = False


N = int(input())
tot_case = 0
row_flag = [0 for _ in range(N)]
col_flag = [False for _ in range(N)]
n_queen()
print(tot_case)