import sys
input = sys.stdin.readline

def room_greedy():

	sorted_times = sorted(times, key=lambda x: (x[1], x[0]))
    
	cnt = 1
	time = sorted_times[0][1]
	for i in range(1, N):
		if time <= sorted_times[i][0]:
			time = sorted_times[i][1]
			cnt += 1
	return cnt

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
print(room_greedy())