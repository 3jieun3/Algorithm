# 뒤에 있는 글자는 패턴 한번으로 가능
# 앞에 있는 글자는 패턴 한번 더 추가

def Greedy():
	s_arr = list(S)
	min_k = 1
	ch = s_arr[0]
	for i in range(1, len(s_arr)):
		if s_arr[i] <= ch:
			min_k += 1
		ch = s_arr[i]
	return min_k


S = input()
print(Greedy())