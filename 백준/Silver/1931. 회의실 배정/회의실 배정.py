import sys
input = sys.stdin.readline

n = int(input())
meeting = []
for _ in range(n):
    meeting.append(list(map(int, input().split())))
# 시작 기준으로 정렬 후 종료 기준으로 정렬 하면
meeting = sorted(meeting, key = lambda x: (x[1], x[0]))
# => 종료 기준 정렬, 같은 종료시간의 경우 시작 시간 오름차순으로 정렬됨
# [14, 14] [12, 14] 둘다 선택되기 위함

end = 0
cnt = 0
for m in meeting:
    # 이전회의 종료시간 후의 시작시간 회의 선택
    if end <= m[0]:
        end = m[1]
        cnt += 1
    
print(cnt)