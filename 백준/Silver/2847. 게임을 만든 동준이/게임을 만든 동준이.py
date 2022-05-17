import sys
input = sys.stdin.readline

N = int(input())
lv_points = [int(input()) for _ in range(N)]

ans = 0
up_point = lv_points[-1]    # 높은 레벨의 점수
for i in range(N - 2, -1, -1):
	if lv_points[i] >= up_point:
		ans += lv_points[i] - (up_point - 1)
		up_point -= 1
	else:
		up_point = lv_points[i]
print(ans)