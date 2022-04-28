def Greedy():
	move = (B - A - 1)
	if (C - B - 1) > move:
		move = (C - B - 1)
	return move

while True:
	try:
		A, B, C = map(int, input().split())
		print(Greedy())
	except:
		break