
def floyd_warshall():
    for k in range(N):   # k : 경유점
        for i in range(N):
            for j in range(N):
                # k 경유해서 i -> j 갈 수 있는 경로 있으면 1 없으면 그대로 0
                if rst[i][k] and rst[k][j]:
                    rst[i][j] = 1


N = int(input())    # 정점의 개수
adj_matrix = [list(map(int, input().split())) for _ in range(N)]
rst = [[0] * N for _ in range(N)]    # i -> j 경로 존재 여부
# 결과 행렬 초기화 : 인접 행렬 이용
for i in range(N):
    for j in range(N):
        if adj_matrix[i][j] == 1:
            rst[i][j] = 1

# 플로이드 와샬
floyd_warshall()

for i in range(N):
    print(*rst[i])