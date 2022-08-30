def solution(board, moves):
    n = len(board)  # 배열 크기
    poped = 0       # 터진 개수
    selected = []   # 선택된 인형 바구니
    
    for c in moves:
        for r in range(n):
            if board[r][c - 1]:           
                selected.append(board[r][c - 1])
                board[r][c - 1] = 0
                # 같은 인형 쌓인 경우
                while len(selected) >= 2 and selected[-2] == selected[-1]:
                    selected.pop()
                    selected.pop()
                    poped += 2
                break
    return poped