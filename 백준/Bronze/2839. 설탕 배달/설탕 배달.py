# sol 2) 그리디

n = int(input())
ans = 0

while n:
    # 5의 배수이면 5로 나누기
    if n%5 == 0:
        ans += n//5
        break
    # 5의 배수가 아니면 3 빼기
    else:
        n -= 3
        ans += 1
        
if ans == 0 or n < 0:
    # 카운트가 0 이거나 5와 3으로 n을 만들수 없는 경우
    print(-1)
else:
    print(ans)