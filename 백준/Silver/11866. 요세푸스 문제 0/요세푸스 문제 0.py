from collections import deque
deq = deque()
n, k = map(int, input().split())

for i in range(1, n+1):
    deq.append(i)

out = []
for _ in range(1, n+1):
    deq.rotate(-k+1)
    out.append(deq.popleft())

st = '<'
for o in out[:n-1]:
    st += str(o)
    st += ', '
st = st + str(out[n-1]) + '>'
print(st)