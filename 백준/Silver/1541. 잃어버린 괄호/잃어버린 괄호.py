import sys
input = sys.stdin.readline
# + 연산을 모두 먼저 -> - 연산
seq = input().split('-')

for i, s in enumerate(seq):
    # + 연산  모두 계산
    if '+' in s:
        tmp = list(map(int, s.split('+')))
        _sum = 0
        for t in tmp: _sum += t
        seq[i] = _sum
    else:
        seq[i] = int(s)

# 남은 원소로 - 연산
rst = seq.pop(0)
while seq:
    rst -= seq.pop(0)
    
print(rst)