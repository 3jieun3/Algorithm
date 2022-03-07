# 스택
t = int(input())
for _ in range(t):
    string = input()
    stack = ['x']
    for i in range(len(string)):
        if string[i] == '(': 
            stack.append('(')
        elif string[i] == ')':
            if stack[-1] == '(':
                del stack[-1]
            else:
                stack.append(')')
    if len(stack) == 1:
        print('YES')
    else:
        print('NO')   