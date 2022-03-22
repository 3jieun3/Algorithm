import sys
input = sys.stdin.readline

def printer():
	for i in range(N):
		q.append((i, arr[i]))       # (인덱스=문서번호, 우선순위)
		priority_cnt[arr[i]] +=1
	out = 0
	print_idx = []
	while len(print_idx) < N:
		doc_id, prior = q[0]
		if sum(priority_cnt[prior + 1:]):
			q.append(q.pop(0))
		else:
			if doc_id == M:
				return len(print_idx) + 1
			else:
				priority_cnt[prior] -= 1
				print_idx.append(doc_id)
				q.pop(0)


TC = int(input())
for _ in range(1, TC + 1):
	N, M = map(int, input().split())
	arr = list(map(int, input().split()))
	q = []
	priority_cnt = [0] * 10
	print(printer())