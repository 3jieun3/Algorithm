# 원형 그래프 -> 하나의 간선 빼면 모든 정점 방문 가능

n = int(input())      # 마을수
cost = list(map(int, input().split()))
print(sum(cost) - max(cost))