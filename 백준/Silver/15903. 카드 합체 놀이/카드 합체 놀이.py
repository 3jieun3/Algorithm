import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 카드개수, 합체횟수
array = sorted(list(map(int, input().split())))     # 오름차순 정렬

for _ in range(M):
	tmp = array[0] + array[1]       # 가장 작은 두 수 합체
	array[0] = array[1] = tmp
	array.sort()

print(sum(array))