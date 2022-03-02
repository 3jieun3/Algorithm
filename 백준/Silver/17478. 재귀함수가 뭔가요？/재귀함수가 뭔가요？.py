def chatbot_recur(n, k):    # k: depth
	# depth 마다의 prefix
	prefix = '____' * k

	# 시작
	if k == 0:
		print(f'{response["start"]}')

	# 질문
	print(f'{prefix}{response["quest"]}')

	# 답변
	if k == n:  # 마지막
		print(f'{prefix}{response[n]}')
	else:   # 마지막 전까지
		for res in response[n - 1]:
			print(f'{prefix}{res}')
		# 재귀 호출 ( 마지막에는 재귀 호출 하지 않음 )
		chatbot_recur(n, k + 1)

	# 끝맺음
	print(f'{prefix}{response["end"]}')


N = int(input())  # 1 ≤ N ≤ 50
response = {
	'start': '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.',
	'quest': '"재귀함수가 뭔가요?"',
	(N-1): ['"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
	        '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
	        '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'],
	N: '"재귀함수는 자기 자신을 호출하는 함수라네"',
	'end': '라고 답변하였지.'
}
chatbot_recur(N, 0)