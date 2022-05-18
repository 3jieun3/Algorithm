import sys
input = sys.stdin.readline

string = input().rstrip()

char = ['U', 'C', 'P', 'C']
UCPC_idx = [-1, -1, -1, -1]

i = 0
for j in range(len(string)):
	if string[j] == char[i]:
		UCPC_idx[i] = j
		i += 1
	if i == 4:
		break
if -1 in UCPC_idx:
	print('I hate UCPC')
else:
	print('I love UCPC')