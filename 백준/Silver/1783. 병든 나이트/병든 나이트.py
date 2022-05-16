N, M = map(int, input().split())
max_visit = 1   # 시작점부터 카운트

# 모든 방향 가능 & 이동횟수 4이상 가능
if N >= 3 and M >= 7:
	max_visit += 4 + (M - 7)

# 모든 방향 가능 & 이동횟수 4이상 불가능(열크기모자람)
elif N >= 3 and M < 7:
	max_visit += (M - 1)    # 최대 경우 : 오른쪽 1칸 움직이는 방향만 골라서 이동
	if max_visit > 4:
		max_visit = 4

# 위아래 1칸 이동하는 방법만 가능 -> 이동횟수 4이상 불가능
elif N == 2:
	max_visit += (M - 1) // 2  # 최대 경우 : 위아래 1칸 이동하는 경우만 골라서 이동
	if max_visit > 4:
		max_visit = 4

# 나머지 경우 : N == 1 인경우 모든 방향 불가능

print(max_visit)