n = int(input())
arr = list(map(int, input().split()))

cnt = 0  # 소수 개수

def is_prime_number(x):
    # 2부터 (x-1) 까지의 모든 수를 확인
    for i in range(2, x):
        # x가 해당 수로 나누어떨어지면 소수 아님
        if x % i == 0:
            return False
    return True

for a in arr:
    if a != 1:
        if is_prime_number(a): cnt += 1
        
print(cnt)