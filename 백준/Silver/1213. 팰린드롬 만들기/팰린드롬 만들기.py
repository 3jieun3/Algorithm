eng_name = input()
ln = len(eng_name)

counts = [0] * 26           # 알파벳 카운트
for i in range(ln):
	counts[ord(eng_name[i]) - ord('A')] += 1

odd_cnt = 0	                # 홀수개인 알파벳 개수
for i in range(26):
	if counts[i] % 2:
		odd_cnt += 1

odd_chr = ''
rst = ''
# 길이가 홀수인 경우 - 홀수개인 알파벳 한개 필요 (중간에 한개 위치)
if ln % 2 and odd_cnt != 1:
	rst += "I'm Sorry Hansoo"
# 길이가 짝수인 경우 - 모두 짝수개 알파벳만 필요
elif ln % 2 == 0 and odd_cnt > 0:
	rst += "I'm Sorry Hansoo"
# 팰린드롬 가능
else:
	for i in range(26):
		if counts[i] == 0:
			continue
		if counts[i] % 2:   # 홀수 길이일때 홀수개인 알파벳 저장
			odd_chr = chr(ord('A') + i)
		rst += chr(ord('A') + i) * (counts[i] // 2)
	# 홀수개알파벳 중간에 위치 + 왼쪽의 반대를 오른쪽에 연결
	rst = rst + odd_chr + rst[::-1]
print(rst)