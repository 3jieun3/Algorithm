def Greedy(T):
	for i in range(3):                  
		sec = btn_sec[i]
		if T >= sec:
			count[i] = T // sec
			T %= sec
	if T:                               # T초 못맞춘 경우
		return -1
	ans = ' '.join(map(str, count))     # 맞춘 경우
	return ans


btn_sec = [300, 60, 10]     # A, B, C 버튼의 시간
count = [0, 0, 0]           # 누르는 횟수
print(Greedy(int(input())))