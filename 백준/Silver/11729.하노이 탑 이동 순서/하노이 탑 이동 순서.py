import sys
input = sys.stdin.readline

# n: 옮겨야할 원판 중 가장 큰 것, 목표: before -> after 로 옮겨야함
def hanoi_recur(n, before, after):
	# 원판 1 은 전달된 위치 그대로 1 하나만 옮기면 됨
	if n == 1:
		movement.append([before, after])
		return
	
	# 1, 2, 3 중 before 와 after 에 없는 것을 n-1 이 갔다와야함
	n_1_visit = 0
	for k in [1, 2, 3]:
		if k != before and k != after:
			n_1_visit = k
			break
	
	hanoi_recur(n - 1, before, n_1_visit)
	movement.append([before, after])
	hanoi_recur(n - 1, n_1_visit, after)


N = int(input())
movement = []   # 원판 이동 경로를 저장할 2차원 리스트
hanoi_recur(N, 1, 3)
# 출력
print(len(movement))
for mv in movement:
	print(*mv)