import sys
input = sys.stdin.readline

N, M = map(int, input().split())
running_times = list(map(int, input().split()))

# 가장 큰 강의 길이보다 작은 블루 레이 불가능
l, r = max(running_times), sum(running_times)
while l <= r:
    tmp_k = (l + r) // 2        # 블루 레이 임시 크기
    cnt = 1                     # 블루 레이 개수 카운트
    _sum = 0                    # 블루 레이에 들어갈 강의 길이 합
    for i in range(N):
        # 강의 길이 합하여 블루 레이 임시 크기 이하로 카운트
        if _sum + running_times[i] <= tmp_k:
            _sum += running_times[i]
        else:
            _sum = running_times[i]
            cnt += 1

    if cnt > M:         # 많이 나오면 블루 레이를 더 큰 크기로
        l = tmp_k + 1
    else:               # 적게 나오면 블루 레이를 더 작은 크기로
        r = tmp_k - 1
print(l)                # 가능한 블루 레이 크기 중 최소