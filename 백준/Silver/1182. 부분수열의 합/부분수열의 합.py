import sys
input = sys.stdin.readline

def recur(i, cur_sum):
	global cnt
	if i == N:
		if subseq:
			if cur_sum == S:
				cnt += 1
		return

	subseq.append(numbers[i])
	recur(i + 1, cur_sum + numbers[i])
	subseq.pop()
	recur(i + 1, cur_sum)


N, S = map(int, input().split())
numbers = list(map(int, input().split()))
subseq = []
cnt = 0
recur(0, 0)
print(cnt)