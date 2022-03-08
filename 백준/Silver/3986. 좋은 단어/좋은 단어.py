import sys
input = sys.stdin.readline

def good_words(n):
	good_cnt = 0
	for i in range(n):              # 각 단어 반복
		stack = [words[i][0]]       # 천번째 단어부터 스택에 push
		j = 1
		while j < len(words[i]):    # 다음 단어가 스택 top 의 단어와 같으면 pop = 선이 교차하지 않고 짝 지을 수 있음
			if len(stack) > 0 and stack[-1] == words[i][j]:
				stack.pop()
			else:
				stack.append(words[i][j])
			j += 1

		if not stack:
			good_cnt += 1

	return good_cnt


N = int(input())
words = [list(input().rstrip()) for _ in range(N)]
print(good_words(N))