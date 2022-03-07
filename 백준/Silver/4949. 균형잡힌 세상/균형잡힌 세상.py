def balanced(n):
	stack = []
	for i in range(n):
		if string[i] not in open_bracket and string[i] not in close_bracket:
			continue
		elif string[i] in open_bracket:
			stack.append(string[i])
		else:
			br_idx = 0
			for j in range(2):
				if string[i] == close_bracket[j]:
					br_idx = j
					break

			if len(stack) > 0 and stack[-1] == open_bracket[br_idx]:
				stack.pop()
			else:
				return 'no'
	if stack:
		return 'no'
	else:
		return 'yes'


open_bracket = ['(', '[']
close_bracket = [')', ']']

while True:
	string = input()
	if string == '.':
		break
	else:
		print(balanced(len(string)))