def solution(N, stages):
    
    now = [0] * (N + 2)
    rate = [[0, i] for i in range(N + 1)]
    for s in stages:
        if s > N:
            now[N + 1] += 1     # 모두 클리어한 사용자는 N + 1인덱스로
        else:
            now[s] += 1         # 현재 도전중인 인덱스 + 1
            
    ac = now[N + 1]
    for i in range(N, 0, -1):
        ac += now[i]
        if ac and now[i]:
            rate[i][0] = now[i] / ac
            
    for i in range(1, N + 1):
        mx_i = i
        for j in range(i + 1, N + 1):
            if rate[mx_i][0] < rate[j][0]:
                mx_i = j
            elif rate[mx_i][0] == rate[j][0] and rate[mx_i][1] > rate[j][1]:
                mx_i = j
        rate[mx_i],rate[i] = rate[i],rate[mx_i]
        
    desc_rate = []
    for i in range(1, N + 1):
        desc_rate.append(rate[i][1])
    
    return desc_rate