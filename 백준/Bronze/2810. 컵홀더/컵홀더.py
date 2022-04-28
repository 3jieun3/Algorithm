def Greedy():
	i = 0
	holder = 0              # 컵 홀더 개수
	while i < N:
		if seat[i] == 'S':  # == '*S'
			holder += 1
			i += 1
		else:               # == '*LL'
			holder += 1
			i += 2
	holder += 1             # 마지막 오른쪽 '*'
	return min(N, holder)   # 최대로 사용 = 모든 홀더 사용 or 모든 사람 사용


N = int(input())    # 좌석 수
seat = input()      # 좌석 정보
print(Greedy())