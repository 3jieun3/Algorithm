import sys
input = sys.stdin.readline

N, L = map(int, input().split())                # N: 물 새는 곳, L: 테이프 길이
pos = sorted(list(map(int, input().split())))   # 물 새는 위치

cnt = 0                                         # 테이프 개수
start = pos[0]                                  # 테이프 시작 위치 초기화

for i in range(1, N):
	if pos[i] - start > L - 1:                  # L - 1 내에 붙일 수 있는 최대 위치(양쪽 0.5씩 제외)
		cnt += 1
		start = pos[i]

cnt += 1                                        # 마지막 붙이던 테이프 개수 추가
print(cnt)