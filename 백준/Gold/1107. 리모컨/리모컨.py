import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
temp = []
if M:
    temp = list(map(int, input().split()))

# 고장:0 정상:1
controller = [1] * 10
for t in temp:
    controller[t] = 0

min_cnt = abs(N - 100)                  # 초기화 : 현재 100 과의 차이만큼 +/-
for d in range(abs(N - 100) + 1):       # 현재 채널인 100과의 차이까지만
    for btn in [N + d, N - d]:          
        if btn < 0:
            continue
        flag = True
        for x in list(map(int, list(str(btn)))):
            if controller[x] == 0:      # 고장난 숫자 있으면 불가능
                flag = False
                break
        if flag:                        # 가능한 경우만 체크
            if min_cnt > d + len(list(str(btn))):
                min_cnt = d + len(list(str(btn)))
print(min_cnt)