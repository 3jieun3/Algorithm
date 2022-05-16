import sys
input = sys.stdin.readline

doc = input().rstrip()
word = input().rstrip()

cnt = 0                                     # 단어 개수
i = 0
while i < len(doc):
	if doc[i] == word[0]:                   # word 첫문자와 같은 문자 탐색
		if doc[i:i + len(word)] == word:    # 찾는 word 와 같은 경우
			cnt += 1
			i += len(word)
		else:                               # 다른 경우
			i += 1
	else:
		i += 1

print(cnt)