def eratos_is_prime(x):
    arr = [False] + [True] * x
    arr[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if arr[i]:  # i 가 소수이면
            j = 2
            while (i * j <= x):     # 소수의 배수들은 소수가 아님
                arr[i * j] = False
                j += 1
    return arr[x]

def is_prime(x):
    if x == 1:
        return False
    i = 2
    while i <= (x ** 0.5):
        if x % i == 0:
            return False
        i += 1
    return True
    
def solution(n, k):
    k_num = []
    tmp = ''
    while n:
        if n % k:
            tmp = str(n % k) + tmp
        elif tmp:
            k_num.append(int(tmp))
            tmp = ''
        n //= k
    k_num.append(int(tmp))
    k_num.reverse()
    
    # 소수 개수 체크
    answer = 0
    for i in range(len(k_num)):
        if is_prime(k_num[i]):
            answer += 1
    
    # 소수 개수 체크
    # is_prime = eratos_is_prime(max(k_num))
    # answer = 0
    # for num in k_num:
    #     if is_prime[num]:
    #         answer += 1
        
    return answer