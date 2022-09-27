def solution(dartResult):
    areas = ['S', 'D', 'T']
    answer = 0
    stack = []
    for s in dartResult:
        if s in areas:
            stack.append(stack.pop() ** (areas.index(s) + 1))
        elif s == '*':
            if len(stack) >= 1:
                stack[-1] *= 2
            if len(stack) >= 2:
                stack[-2] *= 2
        elif s == '#':
            stack[-1] *= (-1)
        elif s == '0':
            if stack and stack[-1] == 1:
                stack[-1] = 10
            else:
                stack.append(int(s))
        else:
            stack.append(int(s))
    answer = sum(stack)
    return answer