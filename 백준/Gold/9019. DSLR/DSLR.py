from collections import deque

def dslr(o, n):
    if o == "D":
        return (2 * n) % 10000
    elif o == "S":
        return (n - 1) if n > 0 else 9999
    # 시간초과 해결 -> 문자열 인덱싱을 숫자 연산으로 고침
    elif o == "L":
        # 첫번째 자리수 (1000의 자리)를 1의 자리로
        return (n % 1000) * 10 + (n // 1000)
    else:   # R
        # 마지막 자리수 (1의 자리)를 1000의 자리로
        return (n % 10) * 1000 + (n // 10)

def bfs(A, B):
    que = deque([(A, "")])
    visited[A] = True
    while que:
        bef, bef_op = que.popleft()     # 한 turn 이 끝난 값, 명령어
        if bef == B:          # 종료 조건
            return bef_op
        for o in ["D", "S", "L", "R"]:  # 한 turn
            aft = dslr(o, bef)
            if not visited[aft]:
                visited[aft] = True
                que.append((aft, bef_op + o))

T = int(input())
for tc in range(T):
    # 메모리, 시간 초과 해결 -> 방문배열
    visited = [False] * 10000
    print(bfs(*map(int, input().split())))
