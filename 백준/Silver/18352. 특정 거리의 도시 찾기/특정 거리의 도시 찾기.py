import sys
import heapq
input = sys.stdin.readline

INF = 999999999

def dijkstra():
	# 출발점
	distance[X] = 0                     # 자기자신으로의 최단거리는 0
	heapq.heappush(min_heap, (0, X))

	while min_heap:                     # 최소가중치 정점이 heap 에 쌓여있을 때만 반복
		# 출발점으로부터의 최단거리(최소가증치) 와 그 정점 dequeue
		min_dist, min_vtx = heapq.heappop(min_heap)
		visited[min_vtx] = 1                            # 최단거리 정점 방문처리

		if distance[min_vtx] + 1 > K:                   # 거리가 K 초과하면 종료
			return

		for vtx in cities[min_vtx]:
			# 새로 방문한 최단거리 정점에서 인접하며 방문하지 않았던 정점까지의 거리(가중치) 갱신
			if visited[vtx] == 0:
				if distance[vtx] > distance[min_vtx] + 1:
					distance[vtx] = distance[min_vtx] + 1       # 모든 도로 거리 1
					heapq.heappush(min_heap, (distance[vtx], vtx))


N, M, K, X = map(int, input().split())
cities = [[] for _ in range(N + 1)]
for i in range(M):
	a, b = map(int, input().split())
	cities[a].append(b)     # a -> b

visited = [0] * (N + 1)
distance = [INF] * (N + 1)      # 거리(가중치)
min_heap = []
dijkstra()

temp = []                       # 최단 거리 K인 도시 찾기
for i in range(1, N + 1):
	if distance[i] == K:
		temp.append(i)
if temp:
	print(*temp, sep="\n")
else:
	print(-1)