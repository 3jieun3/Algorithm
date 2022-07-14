X, Y = map(int, input().split())
Z = int(Y * 100 / X)  # 승률

l, r = 1, 1000000000
rst = -1            # 안되는 경우로 초기화
while l <= r:
    more = (l + r) // 2     # 중간값 : 더 해야할 횟수
    new_z = int((Y + more) * 100 / (X + more))  # 새로운 승률 계산

    if new_z == Z:                   # 승률 같게 나오는 경우 - 더 많은 횟수로
        l = more + 1
    else:                           # 승률 더 많이 나오는 경우 - 더 작은 횟수로
        r = more - 1
        rst = more

print(rst)