import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    numbers_1 = sorted(list(map(int, input().split())))
    M = int(input())
    numbers_2 = list(map(int, input().split()))

    results = [0] * M
    for i in range(M):
        target = numbers_2[i]
        # 각 target 마다 이분 탐색
        l, r = 0, N - 1
        while l <= r:
            mid = (l + r) // 2
            if target == numbers_1[mid]:
                results[i] = 1
                break
            if target >= numbers_1[mid]:
                l = mid + 1
            else:
                r = mid - 1
    print(*results, sep="\n")