import heapq

N, M = map(int, input().split())        # 선물 상자 수, 아이들 수
C = list(map(int, input().split()))     # 상자의 선물 개수
W = list(map(int, input().split()))     # 아이들 원하는 선물 개수

# 최대힙 생성
mx_heap = []
for i in range(N):
    heapq.heappush(mx_heap, (C[i] * (-1), C[i]))
# 선물 가져가기
success_flag = 1
for i in range(M):
    cnt = heapq.heappop(mx_heap)[1]
    if cnt > W[i]:
        cnt -= W[i]
        heapq.heappush(mx_heap, (cnt * (-1), cnt))
    elif cnt < W[i]:
        success_flag = 0
        break
print(success_flag)