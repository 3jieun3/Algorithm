import sys
input = sys.stdin.readline

def func(cnt, arr, cur_num):
	global max_num, min_num

	if cnt == k + 1:
		if min_num > cur_num:
			min_num = cur_num
		if max_num < cur_num:
			max_num = cur_num
		return

	s, e = 0, 10
	if cnt and signs[cnt - 1] == '<':
		s, e = arr[-1] + 1, 10
	if cnt and signs[cnt - 1] == '>':
		s, e = 0, arr[-1]

	for i in range(s, e):
		if bit[i] == 1:
			continue

		bit[i] = 1
		func(cnt + 1, arr + [i], cur_num * 10 + i)
		bit[i] = 0


k = int(input())
signs = input().split()
bit = [0] * 10
max_num, min_num = 0, 99999999999
func(0, [], 0)
print(str(max_num).zfill(k + 1))
print(str(min_num).zfill(k + 1))