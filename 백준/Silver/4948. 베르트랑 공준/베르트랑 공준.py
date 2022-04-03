# 베르트랑 공준
import math

def is_prime_number(x1, x2): 
    arr = [True]*(x2+1)
    for i in range(2, int(math.sqrt(x2))+1):
        if arr[i] == True:
            j = 2
            while (i*j)<=x2:
                arr[i*j] = False
                j += 1
    return [i for i in range(x1, x2+1) if arr[i]] # x1 이상 x2 이하

while True:
    n = int(input())
    if n == 0: break
    print(len(is_prime_number(n+1, n*2))) # n+1 이상 2n 이하