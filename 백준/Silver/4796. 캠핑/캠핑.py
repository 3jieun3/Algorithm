import sys;
input = sys.stdin.readline

result = []
while True:
	L, P, V = map(int, input().split())
	if L == 0 and P == 0 and V == 0:
		break
	q, r = V // P, V % P    # 연속하는 P일동안 L일 사용 세트
	if L < r:               # 사용가능일수 < 남은휴가일수
		result.append(q * L + L)
	else:                   # 남은휴가일수 < 사용가능일수
		result.append(q * L + r)

for tc in range(len(result)):
	print(f'Case {tc + 1}: {result[tc]}')