import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0 
end = max(tree)-1
while start <= end:
    mid = (start + end)//2
    rst = 0
    for t in tree:
        if t > mid:
            rst += (t-mid)
    if rst >= m:
        start = mid+1
    else:
        end = mid-1

print(end)