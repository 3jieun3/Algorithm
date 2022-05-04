def Greedy():
	ppap = 0
	for i in range(n - 3):
		if used[i]:
			continue
		if things[i] != 'p':
			used[i] += 1
			continue

		if things[i:i+4] == 'pPAp':
			ppap += 1
			for j in range(i, i + 4):
				used[j] += 1
	return ppap


n = int(input())
things = input()
used = [0] * n
print(Greedy())