def title(n):
    cnt = 0
    x = 0
    while True:
        x += 1
        if '666' in str(x):
            cnt += 1
        if cnt == n:
            return x
        
print(title(int(input())))