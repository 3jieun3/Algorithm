# top-down
A, B = map(int, input().split())
b = B
cnt = 1             # 1먼저 더해두기
while b > A:
	if b % 2:       # 홀수인 경우
		if b % 10 != 1:
			break
		b //= 10
	else:           # 짝수인 경우
		b //= 2
	cnt += 1
if b == A:
	print(cnt)
else:
	print(-1)