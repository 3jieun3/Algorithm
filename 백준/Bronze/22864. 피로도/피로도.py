def Greedy():
	m_arr = [0] * 25
	j_arr = [0] * 25
	for h in range(1, 25):
		if m_arr[h - 1] + A <= M:
			m_arr[h] = m_arr[h - 1] + A
			j_arr[h] = j_arr[h - 1] + B
		else:
			m_arr[h] = m_arr[h - 1] - C
			if m_arr[h] < 0:
				m_arr[h] = 0
			j_arr[h] = j_arr[h - 1]
	return j_arr[24]

A, B, C, M = map(int, input().split())
print(Greedy())