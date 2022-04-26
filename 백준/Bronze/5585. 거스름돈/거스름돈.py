money = [500, 100, 50, 10, 5, 1]

def Greedy_Change(change):
	cnt = 0                     # 잔돈 개수
	for i in range(6):          # 큰 잔돈부터 줄 수 있는 만큼 주기
		x = money[i]
		if change >= x:
			cnt += change // x
			change %= x
	return cnt


print(Greedy_Change(1000 - int(input())))