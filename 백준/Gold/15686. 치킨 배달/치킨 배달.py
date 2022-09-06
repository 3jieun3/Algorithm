import sys
from itertools import combinations
input = sys.stdin.readline

def calcul_dist():
    for i in range(len(houses)):
        for j in range(len(chickens)):
            distance[i][j] = abs(houses[i][0] - chickens[j][0]) + abs(houses[i][1] - chickens[j][1])


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]  # 1 집, 2 치킨집

# 치킨집, 집 위치 저장
chickens = []
houses = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

# dij = i집(행) ~ j치킨집(열) 사이의 거리
distance = [[0] * len(chickens) for _ in range(len(houses))]
calcul_dist()

min_dist = 999999999
for cnt in range(1, M + 1):
    # 선택된 cnt 개의 치킨집 조합
    for combi in combinations([x for x in range(len(chickens))], cnt):
        cur_dist = 0
        # 각 집에서
        for h_idx in range(len(houses)):
            mn_d = 999999999
            # 선택된 치킨집들 중 최소 거리들의 합
            for v in combi:
                if mn_d > distance[h_idx][v]:
                    mn_d = distance[h_idx][v]
            cur_dist += mn_d
            # 가지치기
            if cur_dist > min_dist:
                break
        # 최소 치킨거리 갱신
        if min_dist > cur_dist:
            min_dist = cur_dist

print(min_dist)