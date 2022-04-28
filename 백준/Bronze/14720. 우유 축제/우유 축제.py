def Greedy():
	cnt = 0
	nxt = 0
	for i in range(N):
		if store[i] == nxt:
			cnt += 1
			nxt = (nxt + 1) % 3

	return cnt


N = int(input())
store = list(map(int, input().split()))     # 0: 딸기, 1: 초코, 2:바나나
print(Greedy())