stack = []
k = int(input())
for _ in range(k):
    n = int(input())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()
rst = 0
for s in stack:
    rst += s
print(rst)