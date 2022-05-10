RSP = ['S', 'R', 'P']

R = int(input())
my_rounds = list(input())
N = int(input())
fr_rounds = [list(input()) for _ in range(N)]

my_score, max_score = 0, 0
for r in range(R):
	me = RSP.index(my_rounds[r])
	score = [0, 0, 0]   # r판에서 상근이가 i 냈을때 얻을 수 있는 점수
	for i in range(N):
		you = RSP.index(fr_rounds[i][r])
		if (you + 1) % 3 == me:  # 이긴 경우
			my_score += 2
		elif me == you:  # 비긴 경우
			my_score += 1

		for m in range(3):
			if (you + 1) % 3 == m:
				score[m] += 2
			elif m == you:
				score[m] += 1
	max_score += max(score)

print(my_score)
print(max_score)