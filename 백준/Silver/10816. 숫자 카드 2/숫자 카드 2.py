# 딕셔너리
n = int(input())
sang = list(map(int, input().split()))
sang.sort()

m = int(input())
target = list(map(int, input().split()))

dic = dict()

for k in sang:
    if k in dic: dic[k] += 1
    else: dic[k] = 1

for t in target:
    if t in dic: print(dic[t], end = ' ')
    else: print('0', end = ' ')