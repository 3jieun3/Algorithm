######################
#  a b c d |  e f g
# [------> | <-----]
#   left      right
######################

import sys
input = sys.stdin.readline

def editor(n, m):
	right_stack = []                    # cursor 기준 오른쪽
	left_stack = list(string)           # cursor 기준 왼쪽
	top = n-1                           # left_stack 의 top (cursor 위치 = stack top의 다음 인덱스)
	for i in range(m):
		command = commands[i]
		if command == 'L':              # cursor 왼쪽으로 한 칸 = 왼쪽 문자 하나가 오른쪽으로
			if top > -1:                # = cursor가 문장 맨 앞이 아닌 경우
				right_stack.append(left_stack.pop())
				top -= 1
		elif command == 'D':            # cursor 오른쪽으로 한 칸 = 오른쪽 문자 하나가 왼쪽으로
			if len(right_stack) > 0:    # = cursor가 문장 맨 뒤가 아닌 경우
				left_stack.append(right_stack.pop())
				top += 1
		elif command == 'B':            # cursor 왼쪽 문자 삭제
			if top > -1:
				left_stack.pop()
				top -= 1
		else:                           # 명령어 마지막 문자를 왼쪽에 추가
			left_stack.append(command[-1])
			top += 1
	return ''.join(left_stack) + ''.join(right_stack[::-1])


string = input().rstrip()                        # 입력된 문자열
M = int(input())                                 # 입력할 명령어 개수
commands = [input().rstrip() for _ in range(M)]  # 입력할 명령어
print(editor(len(string), M))