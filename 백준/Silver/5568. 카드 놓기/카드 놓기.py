import sys
input = sys.stdin.readline

# 조합 - i: depth/index, cnt: 현재 선택한 개수
def combi_recur(i, cnt):
	if i == N:
		if cnt == K:    # 2개 선택된 경우 - 해당 카드 숫자로 이루어진 리스트 생성 (예: '1', '2')
			nums = [str(cards[j]) for j in range(N) if bit[j] == 1]
			perm_swap_recur(0, nums)    # 카드 숫자의 순열 탐색(예: '12', '21')
		return

	bit[i] = 0  # [i] 카드 선택 안함
	combi_recur(i + 1, cnt)
	bit[i] = 1  # [i] 카드 선택함
	combi_recur(i + 1, cnt + 1)


# 순열 - i: depth/index, cnt: 현재 선택한 개수
def perm_swap_recur(i, arr):
	if i == len(arr):
		num = ''.join(arr)
		if num not in selected_nums:    # 조합된 적이 없는 정수만 저장
			selected_nums.append(num)
		return

	for j in range(i, len(arr)):
		arr[i], arr[j] = arr[j], arr[i]
		perm_swap_recur(i + 1, arr)
		arr[i], arr[j] = arr[j], arr[i]


N = int(input())
K = int(input())
cards = [int(input()) for _ in range(N)]
bit = [0] * N   # cards 리스트의 각 카드 = bit 리스트의 i 인덱스 원소
selected_nums = []  # 만들어진 정수
combi_recur(0, 0)
print(len(selected_nums))