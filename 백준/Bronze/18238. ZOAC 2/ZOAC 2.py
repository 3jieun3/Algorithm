def Greedy(n):
	min_move = 0
	target, now = 0, 0
	for i in range(n):
		target = ord(string[i]) - ord('A')
		# Z -> A 넘어가지 않는 방향으로의 거리와 그 반대방향 ( Z -> A 넘어가는 방향 )의 거리 중 최소
		min_move += min(abs(target - now), 26 - abs(target - now))
		now = target
	return min_move


string = input()
print(Greedy(len(string)))