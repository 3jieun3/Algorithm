string = list(map(int, list(input())))
bit_group = [0, 0]  # 0 그룹, 1 그룹
bit_group[string[0]] += 1
for i in range(1, len(string)):
	if string[i - 1] != string[i]:
		bit_group[string[i]] += 1

if 0 in bit_group:      # 이미 모두 같은 숫자인 경우
	print(0)
else:                   # 적은 그룹을 뒤집기
	print(min(bit_group))