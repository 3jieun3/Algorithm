def sum_bruteforce():
	# 1 부터 N 까지 모든 수의 분해합 계산
	for num in range(1, N + 1):
		digit_sum = num
		m = num
		while m > 0:
			digit_sum += m % 10
			m //= 10
		# N 이 나오면 반환
		if digit_sum == N:
			return num
	return 0


N = int(input())
print(sum_bruteforce())