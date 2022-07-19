def solution(id_list, report, k):
    n = len(id_list)
    mail_rst = [0] * n
    
    matrix = [[0] * n for _ in range(n)]  # 신고 행렬
    get_counts = [0] * n     # 신고 당한 횟수
    # 신고 관계 저장
    for i in range(len(report)):
        fr_id, to_id = report[i].split()
        fr = id_list.index(fr_id)
        to = id_list.index(to_id)
        if matrix[fr][to] == 0:     # 중복 신고 제외
            matrix[fr][to] = 1      # fr 이 to 를 신고
            get_counts[to] += 1     # to 가 신고 당한 횟수 저장
    
    # 정지 여부 판단
    stop_id = [False] * len(id_list)
    for i in range(len(id_list)):
        if get_counts[i] >= k:
            stop_id[i] = True
    
    # 메일
    for i in range(len(id_list)):
        for j in range(len(id_list)):
            if stop_id[j] and matrix[i][j] == 1:    # i가 신고한 사람 중에 정지된 사람
                mail_rst[i] += 1
                
    return mail_rst