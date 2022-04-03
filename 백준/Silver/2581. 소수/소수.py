import math

def is_prime_number(x):
    if x == 1: 
        return False
    else:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True

m = int(input())
n = int(input())
p_cnt = 0 # 소수 개수
p_sum = 0 # 소수들의 합
p_min = 0 # 소수 중 최솟값

for a in range(m, n+1):
    if is_prime_number(a):
        if p_min == 0: p_min = a
        p_cnt += 1
        p_sum += a
        
if p_cnt == 0: print('-1')
else:
    print(p_sum)
    print(p_min)