import sys
sys.setrecursionlimit(100000)

n = int(input())
def facto(x):
    if x <= 1:
        return 1
    return x*facto(x-1)

print(facto(n))